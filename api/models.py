import uuid
from io import BytesIO
from pathlib import Path

from django.core.files import File
from django.db import models
from django.db.models.fields.files import ImageFieldFile
from PIL import Image as PillowImage

from api.utils.image_extensions import image_types


class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(upload_to="pictures/", null=True, blank=True)
    title = models.CharField(max_length=255)
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.title} ({self.width}x{self.height})"

    def save(self, *args, **kwargs):
        self.image_resize(self.picture)
        super().save(*args, **kwargs)

    def image_resize(self, image: ImageFieldFile):
        img: PillowImage = PillowImage.open(image)
        image_size: tuple = (self.width, self.height)
        new_image: PillowImage = img.resize(image_size)
        image_extension: str = Path(image.file.name).name.split(".")[-1]
        image_filename: str = f"{self.id}.{image_extension}"
        image_format: str = image_types[image_extension]
        buffer: BytesIO = BytesIO()
        new_image.save(buffer, format=image_format)
        file_object: File = File(buffer)
        image.save(image_filename, file_object, save=False)

    @property
    def get_picture_url(self) -> str:
        return self.picture.url
