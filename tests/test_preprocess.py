import numpy as np
import pytest

from vision.preprocess import (
    validate_frame,
    mirror_frame,
    convert_bgr_to_rgb
)


def test_validate_none():

    with pytest.raises(ValueError):
        validate_frame(None)


def test_validate_empty():

    with pytest.raises(ValueError):
        validate_frame(np.array([]))


def test_validate_wrong_type():

    with pytest.raises(TypeError):
        validate_frame("frame")


def test_mirror():

    img = np.zeros((100, 100, 3), dtype=np.uint8)

    result = mirror_frame(img)

    assert result.shape == img.shape


def test_rgb_conversion():

    img = np.zeros((100, 100, 3), dtype=np.uint8)

    rgb = convert_bgr_to_rgb(img)

    assert rgb.shape == img.shape