"""
MediaPipe Hand Detector.

Responsible only for detecting hands and returning
structured information.
"""

from typing import List

import mediapipe as mp
import numpy as np

from .config import VisionConfig
from .models import Landmark, DetectedHand
from .utils import calculate_bounding_box


class MediaPipeHandDetector:
    """
    Wrapper around MediaPipe Hands.
    """

    def __init__(self, config: VisionConfig):

        self.config = config

        self.mp_hands = mp.solutions.hands

        self.detector = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=config.max_hands,
            min_detection_confidence=config.min_detection_confidence,
            min_tracking_confidence=config.min_tracking_confidence,
        )

    # =====================================================
    # Helpers
    # =====================================================

    def _extract_landmarks(self, hand_landmarks) -> List[Landmark]:
        """
        Convert MediaPipe landmarks into our Landmark dataclass.
        """

        landmarks = []

        for idx, lm in enumerate(hand_landmarks.landmark):
            landmarks.append(
                Landmark(
                    id=idx,
                    x=lm.x,
                    y=lm.y,
                    z=lm.z,
                )
            )

        return landmarks

    # =====================================================
    # Detection
    # =====================================================

    def detect(self, rgb_frame: np.ndarray) -> List[DetectedHand]:
        """
        Detect hands in an RGB frame.
        """

        # Image dimensions (needed for bounding box calculation)
        image_height, image_width = rgb_frame.shape[:2]

        # Run MediaPipe
        results = self.detector.process(rgb_frame)
        
        detected_hands = []

        if not results.multi_hand_landmarks:
            return detected_hands

        for hand_landmarks, handedness in zip(
            results.multi_hand_landmarks,
            results.multi_handedness,
        ):

            landmarks = self._extract_landmarks(hand_landmarks)

            bbox = calculate_bounding_box(
                landmarks,
                image_width,
                image_height,
                padding=self.config.bbox_padding,
            )

            classification = handedness.classification[0]

            detected_hands.append(
                DetectedHand(
                    handedness=classification.label,
                    confidence=classification.score,
                    bounding_box=bbox,
                    landmarks=landmarks,
                )
            )

        return detected_hands

    # =====================================================
    # Cleanup
    # =====================================================

    def close(self):
        self.detector.close()