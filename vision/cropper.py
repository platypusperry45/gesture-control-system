"""
Hand cropper.

Responsible for extracting a hand region from an RGB frame,
padding it to a square while preserving aspect ratio,
and resizing it to the configured size.
"""

import cv2
import numpy as np

from .config import VisionConfig
from .models import BoundingBox


class HandCropper:
    def __init__(self, config: VisionConfig):
        self.target_size = config.crop_size

    def crop(
        self,
        rgb_frame: np.ndarray,
        bbox: BoundingBox,
    ) -> np.ndarray:

        roi = rgb_frame[
            bbox.ymin:bbox.ymin + bbox.height,
            bbox.xmin:bbox.xmin + bbox.width,
        ]

        if roi.size == 0:
            return np.zeros(
                (
                    self.target_size[1],
                    self.target_size[0],
                    3,
                ),
                dtype=np.uint8,
            )

        h, w = roi.shape[:2]

        max_dim = max(h, w)

        pad_top = (max_dim - h) // 2
        pad_bottom = max_dim - h - pad_top

        pad_left = (max_dim - w) // 2
        pad_right = max_dim - w - pad_left

        square = cv2.copyMakeBorder(
            roi,
            pad_top,
            pad_bottom,
            pad_left,
            pad_right,
            cv2.BORDER_CONSTANT,
            value=[0, 0, 0],
        )

        crop = cv2.resize(
            square,
            self.target_size,
            interpolation=cv2.INTER_AREA,
        )

        return crop