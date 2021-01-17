from django.db.models import Q
from django_filters import FilterSet, filters
from rest_framework import mixins, viewsets

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from videos.models.video import Video
from videos.serializers.video import VideoSerializer


class VideoFilter(FilterSet):
    title = filters.CharFilter(method="search_keyword", label="Title")

    class Meta:
        model = Video
        fields = {"title"}

    def search_keyword(self, queryset, name, value):
        my_filter = Q(title__icontains=value) | Q(description__icontains=value)
        return queryset.filter(my_filter)


class VideoViewSet(
    mixins.ListModelMixin, viewsets.GenericViewSet,
):
    queryset = Video.objects.all().order_by("-publishedTime")
    serializer_class = VideoSerializer
    filter_class = VideoFilter
