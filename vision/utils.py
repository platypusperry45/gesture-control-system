"""
Utility functions for the Vision Layer.

Contains reusable mathematical and coordinate helper functions
used throughout the gesture recognition pipeline.

Author: Akshat Yadav
Project: Gesture-Based Desktop Control System
"""

from __future__ import annotations

from typing import List, Tuple

from .models import BoundingBox, Landmark

import numpy as np

def clamp(value: int, minimum: int, maximum: int) -> int:
    """
    Clamp a value between minimum and maximum.
    """

    return max(minimum, min(value, maximum))


def normalized_to_pixel(
    x: float,
    y: float,
    image_width: int,
    image_height: int,
) -> Tuple[int, int]:
    """
    Convert normalized MediaPipe coordinates to pixel coordinates.

    Parameters
    ----------
    x, y : float
        Normalized coordinates in range [0,1]

    image_width : int
    image_height : int

    Returns
    -------
    Tuple[int, int]
        Pixel coordinates.
    """

    px = int(x * image_width)
    py = int(y * image_height)

    return px, py


def pixel_to_normalized(
    x: int,
    y: int,
    image_width: int,
    image_height: int,
) -> Tuple[float, float]:
    """
    Convert pixel coordinates to normalized coordinates.
    """

    return x / image_width, y / image_height


def calculate_bounding_box(
    landmarks: List[Landmark],
    image_width: int,
    image_height: int,
    padding: int = 20,
) -> BoundingBox:
    """
    Calculate bounding box from hand landmarks.
    """

    x_coords = np.clip(x_coords, 0, 1)
    y_coords = np.clip(y_coords, 0, 1)
    
    xmin = int(np.min(x_coords) * image_width)
    xmax = int(np.max(x_coords) * image_width)
    ymin = int(np.min(y_coords) * image_height)
    ymax = int(np.max(y_coords) * image_height)


    xmin = clamp(xmin - padding, 0, image_width)
    ymin = clamp(ymin - padding, 0, image_height)

    xmax = clamp(xmax + padding, 0, image_width)
    ymax = clamp(ymax + padding, 0, image_height)

    return BoundingBox(
        xmin=xmin,
        ymin=ymin,
        width=xmax - xmin,
        height=ymax - ymin,
    )


def calculate_hand_center(
    bbox: BoundingBox,
) -> Tuple[int, int]:
    """
    Compute center point of a bounding box.
    """

    center_x = bbox.xmin + bbox.width // 2
    center_y = bbox.ymin + bbox.height // 2

    return center_x, center_y