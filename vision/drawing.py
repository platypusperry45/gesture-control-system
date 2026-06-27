"""
Drawing utilities for the Vision Layer.

Responsible only for visualizing detection results.
"""

from __future__ import annotations

import cv2
import numpy as np

from .config import VisionConfig
from .models import FrameResult


def draw_features(
    frame: np.ndarray,
    result: FrameResult,
    config: VisionConfig,
) -> np.ndarray:
    """
    Draw landmarks, bounding boxes, handedness and FPS
    onto a BGR frame.

    Returns
    -------
    np.ndarray
        Annotated BGR frame.
    """

    annotated = frame.copy()

    # ---------------- FPS ---------------- #

    if config.draw_fps:
        cv2.putText(
            annotated,
            f"FPS: {int(result.fps)}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

    # ------------ Draw Each Hand ----------- #

    for hand in result.hands:

        bbox = hand.bounding_box

        # Bounding Box
        if config.draw_bounding_boxes:

            cv2.rectangle(
                annotated,
                (bbox.xmin, bbox.ymin),
                (
                    bbox.xmin + bbox.width,
                    bbox.ymin + bbox.height,
                ),
                (255, 0, 0),
                2,
            )

        # Handedness
        if config.draw_handedness:

            label = (
                f"{hand.handedness} "
                f"({hand.confidence:.2f})"
            )

            cv2.putText(
                annotated,
                label,
                (
                    bbox.xmin,
                    max(20, bbox.ymin - 10),
                ),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (255, 0, 0),
                2,
            )

        # Landmarks
        if config.draw_landmarks:

            for lm in hand.landmarks:

                px = int(
                    lm.x * annotated.shape[1]
                )

                py = int(
                    lm.y * annotated.shape[0]
                )

                cv2.circle(
                    annotated,
                    (px, py),
                    4,
                    (0, 0, 255),
                    -1,
                )

    return annotated