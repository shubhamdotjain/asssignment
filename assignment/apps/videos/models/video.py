from django.db import models


class Video(models.Model):
    title = models.TextField()
    description = models.TextField()
    publishedTime = models.DateTimeField(auto_now=False)
    videoId = models.TextField(primary_key=True)
    channelId = models.TextField()

    createdOn = models.DateTimeField(auto_now_add=True, editable=False)
    updatedOn = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "Videos"
        indexes = [
            models.Index(fields=["publishedTime", "title"]),
        ]

    def __str__(self):
        return self.title


class VideoThumbNail(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name="thumbnail")
    screenType = models.CharField(max_length=20)
    url = models.TextField()
    height = models.IntegerField()
    width = models.IntegerField()

    createdOn = models.DateTimeField(auto_now_add=True, editable=False)
    updatedOn = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "VideoThumbNails"

    def __str__(self):
        return self.video.title + self.screenSize
