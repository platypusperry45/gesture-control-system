"""
Quality Filter.

Determines whether a detected hand should be
accepted for dataset collection.
"""

from __future__ import annotations

import numpy as np

from vision.models import HandData

from dataclasses import dataclass

from .config import (
    MIN_CONFIDENCE,
    MIN_HAND_WIDTH,
    MIN_HAND_HEIGHT,
    MIN_CROP_SIZE,
    ALLOW_BORDER_TOUCH,
)

@dataclass(slots=True)
class QualityReport:
    """
    Result of evaluating one detected hand.
    """

    valid: bool

    reason: str

class QualityFilter:
    """
    Performs quality checks on detected hands.
    """

    def __init__(self):

        self.last_reason = "GOOD"

    # ---------------------------------------------------------
    # Confidence
    # ---------------------------------------------------------

    def confidence_ok(
        self,
        hand: HandData,
    ) -> bool:

        if hand.confidence >= MIN_CONFIDENCE:

            return True

        self.last_reason = "LOW CONFIDENCE"

        return False

    # ---------------------------------------------------------
    # Bounding Box Size
    # ---------------------------------------------------------

    def size_ok(
        self,
        hand: HandData,
    ) -> bool:

        box = hand.bounding_box

        if (
            box.width >= MIN_HAND_WIDTH
            and
            box.height >= MIN_HAND_HEIGHT
        ):

            return True

        self.last_reason = "HAND TOO SMALL"

        return False

    # ---------------------------------------------------------
    # Crop Size
    # ---------------------------------------------------------

    def crop_ok(
        self,
        hand: HandData,
    ) -> bool:

        image = hand.cropped_image

        if image is None:

            self.last_reason = "NO CROP"

            return False

        h, w = image.shape[:2]

        if (
            h >= MIN_CROP_SIZE
            and
            w >= MIN_CROP_SIZE
        ):

            return True

        self.last_reason = "CROP TOO SMALL"

        return False

    # ---------------------------------------------------------
    # Inside Frame
    # ---------------------------------------------------------

    def inside_frame(
        self,
        hand: HandData,
        frame_shape,
    ) -> bool:

        if ALLOW_BORDER_TOUCH:

            return True

        height, width = frame_shape[:2]

        box = hand.bounding_box

        if (
            box.xmin <= 0
            or
            box.ymin <= 0
            or
            box.xmin + box.width >= width
            or
            box.ymin + box.height >= height
        ):

            self.last_reason = "HAND OUTSIDE FRAME"

            return False

        return True

    # ---------------------------------------------------------
    # Final Decision
    # ---------------------------------------------------------

    def evaluate(
        self,
        hand: HandData,
        frame_shape,
    ) -> QualityReport:

        self.last_reason = "GOOD"

        if not self.confidence_ok(hand):

            return QualityReport(
                False,
                self.last_reason,
            )

        if not self.size_ok(hand):

            return QualityReport(
                False,
                self.last_reason,
            )

        if not self.crop_ok(hand):

            return QualityReport(
                False,
                self.last_reason,
            )

        if not self.inside_frame(
            hand,
            frame_shape,
        ):

            return QualityReport(
                False,
                self.last_reason,
            )

        return QualityReport(
            True,
            "GOOD",
        )