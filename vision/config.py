"""
Configuration settings for the Vision Layer.
"""

from dataclasses import dataclass
from typing import Tuple


@dataclass(slots=True)
class VisionConfig:
    """
    Stores all configurable parameters for the Vision Layer.
    """

    # ----------------------------
    # Camera
    # ----------------------------
    camera_index: int = 0
    resolution: Tuple[int, int] = (640, 480)
    mirror_image: bool = True

    # ----------------------------
    # MediaPipe Detection
    # ----------------------------
    max_hands: int = 2
    min_detection_confidence: float = 0.7
    min_tracking_confidence: float = 0.5

    # ----------------------------
    # Crop Generation
    # ----------------------------
    crop_size: Tuple[int, int] = (128, 128)
    bbox_padding: int = 20

    # ----------------------------
    # Visualization
    # ----------------------------
    draw_landmarks: bool = True
    draw_bounding_boxes: bool = True
    draw_fps: bool = True
    draw_handedness: bool = True