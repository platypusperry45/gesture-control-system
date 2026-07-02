"""
Vision Pipeline.

The central API of Layer 1.

Pipeline:

BGR Frame
    │
    ▼
Mirror (optional)
    │
    ▼
BGR → RGB
    │
    ▼
MediaPipe Detector
    │
    ▼
Hand Cropper
    │
    ▼
FrameResult
"""

from __future__ import annotations

import time
import numpy as np

from .config import VisionConfig
from .cropper import HandCropper
from .detector import MediaPipeHandDetector
from .fps import FPSCounter
from .models import FrameResult, HandData
from .preprocess import (
    convert_bgr_to_rgb,
    mirror_frame,
)


class VisionPipeline:
    """
    Main API for the Vision Layer.
    """

    def __init__(self, config: VisionConfig | None = None):

        self.config = config or VisionConfig()

        self.detector = MediaPipeHandDetector(self.config)

        self.cropper = HandCropper(self.config)

        self.fps_counter = FPSCounter()

    def process(
        self,
        frame: np.ndarray,
    ) -> FrameResult:
        """
        Process one BGR frame.

        Returns
        -------
        FrameResult
        """

        # Optional mirror
        if self.config.mirror_image:
            frame = mirror_frame(frame)

        # Convert for MediaPipe
        rgb_frame = convert_bgr_to_rgb(frame)

        # Detect hands
        detected_hands = self.detector.detect(rgb_frame)

        hands = []

        for hand in detected_hands:

            crop = self.cropper.crop(
                rgb_frame,
                hand.bounding_box,
            )

            landmarks = np.asarray(
                [[lm.x, lm.y, lm.z] for lm in hand.landmarks],
                dtype=np.float32,
            ).reshape(-1)

            hands.append(
                HandData(
                    handedness=hand.handedness,
                    confidence=hand.confidence,
                    bounding_box=hand.bounding_box,
                    landmarks=landmarks,
                    cropped_image=crop,
                )
            )

        fps = self.fps_counter.update()

        return FrameResult(
            frame=frame,
            timestamp=time.time(),
            fps=fps,
            hands=hands,
        )
    
    def close(self):
        self.detector.close()