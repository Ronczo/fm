import uuid

from django.core.files import File
from pathlib import Path

from io import BytesIO

from django.db import models
from PIL import Image as PillowImage

image_types = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "gif": "GIF",
    "tif": "TIFF",
    "tiff": "TIFF",
}

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    title = models.CharField(max_length=255)
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.title} {self.width}x{self.height}"

    def save(self, *args, **kwargs):
        if self.image_has_wrong_size():
            self.image_resize(self.picture)
        else:
            super().save(*args, **kwargs)

    def image_resize(self, image):
        img = PillowImage.open(image)
        image_size = (self.width, self.height)
        new_image = img.resize(image_size)
        image_extension = Path(image.file.name).name.split(".")[-1]
        image_filename = f"{self.id}.{image_extension}"
        image_format = image_types[image_extension]
        buffer = BytesIO()
        new_image.save(buffer, format=image_format)
        file_object = File(buffer)
        image.save(image_filename, file_object)

    def image_has_wrong_size(self):
        return self.picture.height != self.height or self.picture.width != self.width

    @property
    def get_picture_url(self):
        return self.picture.url

