import os
import pathlib

import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from api.models import Image
from tests.factories import ImageFactory

register(ImageFactory)


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture(autouse=True)
def db(image_factory):
    for _ in range(21):
        image_factory.create()


@pytest.fixture
def first_image():
    return Image.objects.first()


@pytest.fixture
def build_image(image_factory):
    return image_factory.build()


@pytest.fixture
def create_image(image_factory):
    return image_factory.create()


@pytest.fixture(scope="session", autouse=True)
def cleanup():
    yield None
    filepath = pathlib.Path(__file__).resolve().parent.parent
    for file in os.listdir(f"{filepath}/pictures"):
        os.remove(f"{filepath}/pictures/{file}")
    os.rmdir(f"{filepath}/pictures")
