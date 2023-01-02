import pytest

from pytest_factoryboy import register
from rest_framework.test import APIClient

from api.models import Image
from tests.factories import ImageFactory

register(ImageFactory)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def db(image_factory):
    for _ in range(20):
        image_factory.create()

@pytest.fixture
def first_image():
    return Image.objects.first()

@pytest.fixture
def build_image(image_factory):
    return image_factory.build()
