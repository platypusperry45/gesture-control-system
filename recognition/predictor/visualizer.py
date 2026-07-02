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
    # Gesture Label
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

        text = (
            f"{prediction['gesture']} "
            f"({prediction['confidence']:.2f})"
        )

        cv2.putText(
            image,
            text,
            (bbox.xmin, max(25, bbox.ymin - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
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
        Draw landmarks.

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