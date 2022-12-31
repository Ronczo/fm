from django_filters import rest_framework
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import mixins, generics, status
from rest_framework.response import Response

from api.filters import ImageFilter
from api.models import Image
from api.serializers import ImageSerializer, ImageUploadSerializer


class ImageViewSet(mixins.ListModelMixin, generics.GenericAPIView):
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
    ])
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)



    @extend_schema(
        request=ImageUploadSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)



class ImageDetailViewSet(mixins.RetrieveModelMixin, generics.GenericAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

