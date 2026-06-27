import numpy as np

from vision.config import VisionConfig
from vision.cropper import HandCropper
from vision.models import BoundingBox


def test_cropper_output_shape():

    config = VisionConfig()

    cropper = HandCropper(config)

    image = np.zeros(
        (480, 640, 3),
        dtype=np.uint8,
    )

    bbox = BoundingBox(
        xmin=100,
        ymin=100,
        width=150,
        height=200,
    )

    crop = cropper.crop(image, bbox)

    assert crop.shape == (128, 128, 3)