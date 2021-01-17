from django.urls import include, path
from rest_framework import routers
from videos.controllers.video import VideoViewSet
from videos.controllers.key import APIKeyViewSet

router = routers.DefaultRouter()

router.register(r"videos", VideoViewSet, basename="videos")
router.register(r"keys", APIKeyViewSet, basename="keys")


urlpatterns = [
    path("", include(router.urls)),
]

from videos.tasks.get_latest_video import start_searching_and_adding_youtube_videos

# start_searching_and_adding_youtube_videos()
