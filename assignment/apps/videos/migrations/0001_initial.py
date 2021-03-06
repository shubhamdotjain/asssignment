# Generated by Django 3.0.5 on 2021-01-16 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="APIKey",
            fields=[
                ("key", models.TextField(primary_key=True, serialize=False)),
                ("active", models.BooleanField(default=False)),
            ],
            options={
                "db_table": "APIkeys",
            },
        ),
        migrations.CreateModel(
            name="Video",
            fields=[
                ("title", models.TextField()),
                ("description", models.TextField()),
                ("publishedTime", models.DateTimeField()),
                ("videoId", models.TextField(primary_key=True, serialize=False)),
                ("channelId", models.TextField()),
                ("createdOn", models.DateTimeField(auto_now_add=True)),
                ("updatedOn", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "Videos",
            },
        ),
        migrations.CreateModel(
            name="VideoThumbNail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("screenType", models.CharField(max_length=20)),
                ("url", models.TextField()),
                ("height", models.IntegerField()),
                ("width", models.IntegerField()),
                ("createdOn", models.DateTimeField(auto_now_add=True)),
                ("updatedOn", models.DateTimeField(auto_now=True)),
                (
                    "video",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="thumbnail",
                        to="videos.Video",
                    ),
                ),
            ],
            options={
                "db_table": "VideoThumbNails",
            },
        ),
        migrations.AddIndex(
            model_name="video",
            index=models.Index(
                fields=["publishedTime", "title"], name="Videos_publish_5e8e80_idx"
            ),
        ),
    ]
