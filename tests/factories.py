from random import randint
import factory
from api.models import Image


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image

    width: int = randint(100, 300)
    height: int = randint(100, 300)
    title: str = f"test {width} {height}"
    picture = factory.django.ImageField(color='blue', height=300, width=300)
