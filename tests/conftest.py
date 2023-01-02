import pytest

from pytest_factoryboy import register
from rest_framework.test import APIClient

from tests.factories import ImageFactory

register(ImageFactory)

@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def db(image_factory):
    for _ in range(20):
        image_factory.create()




