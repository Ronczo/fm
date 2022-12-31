from django_filters import rest_framework
from rest_framework import mixins, generics, status
from rest_framework.response import Response

from api.filters import ImageFilter
from api.models import Image
from api.serializers import ImageSerializer, ImageUploadSerializer


class ImageViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, generics.GenericAPIView
):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = ImageFilter
    filterset_fields = ("title",)

    def get(self, request, *args, **kwargs):
        if kwargs.get("pk"):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response("The image has been added", status=status.HTTP_201_CREATED)