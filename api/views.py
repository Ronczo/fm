from rest_framework import mixins, generics

from api.filters import ImageFilter
from api.serializers import ImageSerializer
from api.models import Image
from django_filters import rest_framework

class ImageViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_fields = ('title',)

    def get(self, request, *args, **kwargs):

        if kwargs.get("pk"):
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        ...