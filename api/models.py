import uuid
from django.db import models

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.ImageField(upload_to='pictures/', null=True, blank=True)
    title = models.CharField(max_length=255)
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.title} {self.width}x{self.height}"
    @property
    def get_s3_url(self):
        return self.picture.url
