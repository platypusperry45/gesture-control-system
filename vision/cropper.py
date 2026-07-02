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

        h, w = rgb_frame.shape[:2]

        xmin = max(0, bbox.xmin)
        ymin = max(0, bbox.ymin)

        xmax = min(w, bbox.xmin + bbox.width)
        ymax = min(h, bbox.ymin + bbox.height)

        roi = rgb_frame[ymin:ymax, xmin:xmax]

        if roi.size == 0:
           return np.zeros(
            (
                self.target_size[1],
                self.target_size[0],
                3,
            ),
            dtype=np.uint8,
        )

        # Get ROI size
        rh, rw = roi.shape[:2]

        # Make square padding
        max_dim = max(rh, rw)

        pad_top = (max_dim - rh) // 2
        pad_bottom = max_dim - rh - pad_top

        pad_left = (max_dim - rw) // 2
        pad_right = max_dim - rw - pad_left

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
        cv2.imwrite("debug_crop.png", crop)
        return crop