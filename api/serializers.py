from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    url = serializers.URLField(source="get_picture_url")
    class Meta:
        model = Image
        exclude = ["picture"]
        ref_name = "Image serializer"

class ImageUploadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = "__all__"
        ref_name = "Image upload serializer"

