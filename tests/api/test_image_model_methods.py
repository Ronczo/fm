import pytest


@pytest.mark.django_db
def test_image_resize(create_image):
    wanted_image_size: tuple = (create_image.width, create_image.height)
    create_image.image_resize(create_image.picture)
    assert (
        create_image.picture.width,
        create_image.picture.height,
    ) == wanted_image_size


@pytest.mark.django_db
def test_get_picture_url(create_image):
    assert create_image.get_picture_url == create_image.picture.url
