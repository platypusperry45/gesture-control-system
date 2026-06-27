import pytest

from vision.models import Landmark, BoundingBox
from vision.utils import (
    clamp,
    normalized_to_pixel,
    pixel_to_normalized,
    calculate_bounding_box,
    calculate_hand_center,
)


def test_clamp():

    assert clamp(5, 0, 10) == 5
    assert clamp(-5, 0, 10) == 0
    assert clamp(15, 0, 10) == 10


def test_normalized_to_pixel():

    x, y = normalized_to_pixel(0.5, 0.5, 640, 480)

    assert x == 320
    assert y == 240


def test_pixel_to_normalized():

    x, y = pixel_to_normalized(320, 240, 640, 480)

    assert x == 0.5
    assert y == 0.5


def test_bounding_box():

    landmarks = [
        Landmark(0, 0.2, 0.2, 0),
        Landmark(1, 0.8, 0.8, 0),
    ]

    bbox = calculate_bounding_box(
        landmarks,
        100,
        100,
        padding=0,
    )

    assert bbox.xmin == 20
    assert bbox.ymin == 20
    assert bbox.width == 60
    assert bbox.height == 60


def test_hand_center():

    bbox = BoundingBox(
        xmin=20,
        ymin=20,
        width=60,
        height=60,
    )

    center = calculate_hand_center(bbox)

    assert center == (50, 50)