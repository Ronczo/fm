import django_filters

from api.models import Image


class ImageFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Image
        fields = ["title"]
