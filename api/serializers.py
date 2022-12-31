from rest_framework import serializers
from api.models import Image
from api.utils.image_extensions import image_types

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

    def validate(self, attrs):
        try:
            import logging
            logging.warning("test")
            image = attrs['picture']
            extension = str(image).split(".")[-1].lower()
            if extension not in image_types.keys():
                raise serializers.ValidationError('Unsupported image extension')
        except KeyError:
            raise serializers.ValidationError("Image is missing")
        return super().validate(attrs)
