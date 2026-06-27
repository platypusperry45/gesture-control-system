"""
Data models representing the outputs of the Vision Layer.
"""

from dataclasses import dataclass, field
from typing import List
import numpy as np


@dataclass
class Landmark:
    """Represents a single hand landmark."""
    id: int
    x: float
    y: float
    z: float


@dataclass
class BoundingBox:
    """Represents a hand bounding box in pixel coordinates."""
    xmin: int
    ymin: int
    width: int
    height: int


@dataclass
class HandData:
    """Represents one detected hand."""
    handedness: str
    confidence: float
    bounding_box: BoundingBox
    landmarks: List[Landmark]
    cropped_image: np.ndarray = field(repr=False)


@dataclass
class FrameResult:
    """Output of the Vision Pipeline for one processed frame."""
    frame: np.ndarray = field(repr=False)
    timestamp: float
    fps: float
    hands: List[HandData]