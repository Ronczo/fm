import uuid
from django.db import models

class Image(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    picture = models.FileField(upload_to='pictures/', null=True, blank=True)
    title = models.CharField(max_length=255)
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
