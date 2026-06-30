"""
Hand Detector.

Wraps the Vision module for gesture recognition inference.
"""

from __future__ import annotations

import numpy as np

from vision.config import VisionConfig
from vision.detector import MediaPipeHandDetector
from vision.models import DetectedHand


class HandDetector:
    """
    Wrapper around the Vision MediaPipe detector.
    """

    def __init__(
        self,
        config: VisionConfig | None = None,
    ):

        self.detector = MediaPipeHandDetector(

            config or VisionConfig()

        )

    # =====================================================
    # Public API
    # =====================================================

    def detect(
        self,
        image: np.ndarray,
    ) -> DetectedHand | None:
        """
        Returns the first detected hand.

        Returns
        -------
        DetectedHand | None
        """

        hands = self.detector.detect(

            image,

        )

        if not hands:

            return None

        return hands[0]

    # =====================================================
    # Cleanup
    # =====================================================

    def close(self):

        self.detector.close()