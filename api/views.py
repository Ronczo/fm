from django_filters import rest_framework
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins, status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from api.filters import ImageFilter
from api.models import Image
from api.serializers import ImageSerializer, ImageUploadSerializer


class ImageViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    GenericViewSet,
):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = ImageFilter
    filterset_fields = ("title",)

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "title",
                OpenApiTypes.STR,
                description="To search given title. Leave blank to not filter.",
            ),
        ]
    )
    def list(self, *args, **kwargs):
        return super().list(*args, kwargs)

    @extend_schema(request=ImageUploadSerializer)
    def create(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            instance = serializer.save()
            read_serializer = self.serializer_class(instance=instance)
            return Response(read_serializer.data, status=status.HTTP_201_CREATED)
