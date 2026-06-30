"""
Data models representing the outputs of the Vision Layer.
"""

from dataclasses import dataclass, field
from typing import List
import numpy as np


@dataclass
class Landmark:
    id: int
    x: float
    y: float
    z: float


@dataclass
class BoundingBox:
    xmin: int
    ymin: int
    width: int
    height: int


@dataclass
class DetectedHand:
    """
    Raw output from the detector.
    Used before cropping.
    """
    handedness: str
    confidence: float
    bounding_box: BoundingBox
    landmarks: List[Landmark]


@dataclass
class HandData:
    """
    Final processed hand data.
    """
    handedness: str
    confidence: float
    bounding_box: BoundingBox
    landmarks: np.ndarray
    cropped_image: np.ndarray = field(repr=False)


@dataclass
class FrameResult:
    frame: np.ndarray = field(repr=False)
    timestamp: float
    fps: float
    hands: List[HandData]