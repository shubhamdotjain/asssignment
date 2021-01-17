import datetime

from videos.models.key import APIKey
from videos.models.video import Video, VideoThumbNail
from videos.helpers.youtube import youtube_api_helper
from celery import shared_task


def search_youtube(query, limit):
    api_keys = list(APIKey.objects.filter(active=True))
    if not api_keys:
        return {}
    api_obj = api_keys[0]
    response = youtube_api_helper(api_obj.key)

    if not response:
        api_obj.active = False
        api_obj.save()
    return response


def extract_video_thumbnails_from_response(response):
    return [
        {
            "screenType": screen_size,
            "url": response["snippet"]["thumbnails"][screen_size]["url"],
            "height": response["snippet"]["thumbnails"][screen_size]["height"],
            "width": response["snippet"]["thumbnails"][screen_size]["width"],
        }
        for screen_size in response["snippet"]["thumbnails"]
    ]


def extract_video_from_response(response):
    return {
        "title": response["snippet"]["title"],
        "description": response["snippet"]["description"],
        "videoId": response["id"].get("videoId", ""),
        "channelId": response["snippet"]["channelId"],
        "publishedTime": get_date_time_object_from_string(
            response["snippet"]["publishedAt"]
        ),
    }


def get_date_time_object_from_string(date_time):
    return datetime.datetime.strptime(
        date_time.split("T")[0] + " " + date_time.split("T")[1].split("Z")[0],
        "%Y-%m-%d %H:%M:%S",
    )


def add_video_and_thumbail(response):

    video_dict = extract_video_from_response(response)
    video_obj, _ = Video.objects.update_or_create(
        videoId=video_dict.pop("videoId"), defaults=video_dict
    )

    thumbnails = extract_video_thumbnails_from_response(response)
    for thumbnail in thumbnails:
        thumbnail["video"] = video_obj
        thumbnail_obj = VideoThumbNail(**thumbnail)
        thumbnail_obj.save()


def get_time_of_recent_uploaded_video():
    videos = Video.objects.all().order_by("-publishedTime")
    return videos[0].publishedTime if videos else None


def search_and_add_latest_videos():

    recent_time = get_time_of_recent_uploaded_video()
    search_response = search_youtube("ind vs aus ", 10)
    if search_response == {}:
        return
    sorted(search_response, key=lambda i: i["snippet"]["publishedAt"], reverse=True)
    for response in search_response:
        published_time = get_date_time_object_from_string(
            response["snippet"]["publishedAt"]
        )

        if not recent_time or recent_time < published_time:
            add_video_and_thumbail(response)
            recent_time = published_time


@shared_task
def start_searching_and_adding_youtube_videos():
    if list(APIKey.objects.filter(active=True)):
        search_and_add_latest_videos()
