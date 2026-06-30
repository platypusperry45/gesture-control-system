"""
Image Loader.

Loads images for inference.
"""

from __future__ import annotations

from pathlib import Path

import cv2
import numpy as np


class ImageLoader:
    """
    Utility for loading images.
    """

    # =====================================================
    # Public API
    # =====================================================

    @staticmethod
    def load(
        image_path: str | Path,
    ) -> np.ndarray:

        image_path = Path(image_path)

        if not image_path.exists():

            raise FileNotFoundError(

                f"Image not found: {image_path}"

            )

        image = cv2.imread(

            str(image_path),

            cv2.IMREAD_COLOR,

        )

        if image is None:

            raise ValueError(

                f"Failed to load image: {image_path}"

            )

        image = cv2.cvtColor(

            image,

            cv2.COLOR_BGR2RGB,

        )

        return image

    # =====================================================
    # Validation
    # =====================================================

    @staticmethod
    def exists(
        image_path: str | Path,
    ) -> bool:

        return Path(image_path).exists()

    @staticmethod
    def is_rgb(
        image: np.ndarray,
    ) -> bool:

        return (

            image.ndim == 3

            and image.shape[2] == 3

        )

    @staticmethod
    def image_size(
        image: np.ndarray,
    ) -> tuple[int, int]:

        return (

            image.shape[1],

            image.shape[0],

        )