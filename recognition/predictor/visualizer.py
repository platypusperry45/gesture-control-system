"""
Prediction Visualizer.

Draws prediction results on images.
"""

from __future__ import annotations

import cv2
import numpy as np


class Visualizer:
    """
    Draws prediction results.
    """

    # =====================================================
    # Bounding Box
    # =====================================================

    @staticmethod
    def draw_bounding_box(
        image: np.ndarray,
        bbox,
        color=(0, 255, 0),
        thickness=2,
    ) -> None:
        """
        Draw bounding box.
        """

        x1 = bbox.xmin
        y1 = bbox.ymin

        x2 = x1 + bbox.width
        y2 = y1 + bbox.height

        cv2.rectangle(
            image,
            (x1, y1),
            (x2, y2),
            color,
            thickness,
        )

    # =====================================================
    # Prediction Label
    # =====================================================

    @staticmethod
    def draw_prediction(
        image: np.ndarray,
        prediction: dict,
    ) -> None:
        """
        Draw gesture name and confidence.
        """

        bbox = prediction["bounding_box"]

        # Make gesture name human-readable
        gesture = prediction["gesture"].replace("_", " ").title()

        # Convert confidence to percentage
        confidence = prediction["confidence"] * 100

        text = f"{gesture} ({confidence:.1f}%)"

        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 0.65
        thickness = 2

        (text_width, text_height), baseline = cv2.getTextSize(
            text,
            font,
            font_scale,
            thickness,
        )

        x = bbox.xmin
        y = max(30, bbox.ymin - 10)

        # Background rectangle
        cv2.rectangle(
            image,
            (x - 4, y - text_height - 6),
            (x + text_width + 4, y + baseline),
            (0, 0, 0),
            -1,
        )

        # Text
        cv2.putText(
            image,
            text,
            (x, y),
            font,
            font_scale,
            (0, 255, 0),
            thickness,
            cv2.LINE_AA,
        )

    # =====================================================
    # Landmarks
    # =====================================================

    @staticmethod
    def draw_landmarks(
        image: np.ndarray,
        landmarks,
        radius: int = 3,
        color=(0, 0, 255),
    ) -> None:
        """
        Draw hand landmarks.

        Supports:
        - list[Landmark]
        - ndarray (21,3)
        - ndarray (63,)
        """

        height, width = image.shape[:2]

        # ----------------------------
        # NumPy array
        # ----------------------------
        if isinstance(landmarks, np.ndarray):

            if landmarks.shape == (63,):
                landmarks = landmarks.reshape(21, 3)

            elif landmarks.shape != (21, 3):
                raise ValueError(
                    f"Unsupported landmark shape: {landmarks.shape}"
                )

            for x, y, _ in landmarks:

                cv2.circle(
                    image,
                    (
                        int(x * width),
                        int(y * height),
                    ),
                    radius,
                    color,
                    -1,
                )

            return

        # ----------------------------
        # Landmark objects
        # ----------------------------
        for landmark in landmarks:

            cv2.circle(
                image,
                (
                    int(landmark.x * width),
                    int(landmark.y * height),
                ),
                radius,
                color,
                -1,
            )

    # =====================================================
    # Complete Visualization
    # =====================================================

    def draw(
        self,
        image: np.ndarray,
        prediction: dict,
        landmarks,
    ) -> np.ndarray:
        """
        Draw complete prediction.
        """

        self.draw_bounding_box(
            image,
            prediction["bounding_box"],
        )

        self.draw_prediction(
            image,
            prediction,
        )

        self.draw_landmarks(
            image,
            landmarks,
        )

        return image