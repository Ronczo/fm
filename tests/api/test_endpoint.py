from typing import List, Dict, Union

import pytest
from django.conf import settings
from django.db.models.fields.files import ImageFieldFile
from rest_framework.response import Response

from api.models import Image


@pytest.mark.parametrize(
    "filter_settings",
    [
        ("", settings.REST_FRAMEWORK["PAGE_SIZE"]),
        ("test", settings.REST_FRAMEWORK["PAGE_SIZE"]),
        ("some_wrong_filter", 0),
    ],
)
@pytest.mark.django_db
def test_fetching_list(client, filter_settings):
    filter_param = filter_settings[0]
    extected_response_amount = filter_settings[1]
    response: Response = client.get(f"/api/images/?title={filter_param}")
    assert response.status_code == 200

    # check pagination (if exists)
    expected_fields: List[str] = ["count", "next", "previous", "results"]
    assert all(field in response.data.keys() for field in expected_fields)

    # check pagination size and filtering
    assert len(response.data["results"]) == extected_response_amount
    expected_fields_in_object: List[str] = ["id", "url", "title", "width", "height"]
    # Check object structure
    for obj in response.data["results"]:
        assert all(field in obj for field in expected_fields_in_object)


@pytest.mark.django_db
def test_fetching_retrieve(client, first_image):
    response: Response = client.get(f"/api/images/{first_image.id}/")

    assert response.status_code == 200
    # check response structure
    expected_fields: List[str] = ["id", "url", "title", "width", "height"]
    assert all(field in response.data.keys() for field in expected_fields)

    payload: Dict[str, Union[str, int]] = {
        "id": first_image.id,
        "url": first_image.picture.url,
        "title": first_image.title,
        "width": first_image.width,
        "height": first_image.height,
    }
    # check response values
    assert sorted(payload) == sorted(response.data)


@pytest.mark.django_db
def test_post_image(client, build_image):
    image_amount_in_db: int = Image.objects.all().count()
    payload: Dict[str, Union[str, int, ImageFieldFile]] = {
        "title": build_image.title,
        "width": build_image.width,
        "height": build_image.height,
        "picture": build_image.picture,
    }
    response: Response = client.post(f"/api/images/", payload)

    image_amount_in_db_after_post_request: int = Image.objects.all().count()
    #  # image added to db
    assert image_amount_in_db_after_post_request == image_amount_in_db + 1

    # check object structure
    expected_fields: List[str] = ["id", "url", "title", "width", "height"]
    assert all(field in response.data.keys() for field in expected_fields)

    # check response values
    for key, value in payload.items():
        if key != "picture":
            assert value == response.data[key]
