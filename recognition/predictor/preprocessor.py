"""
Preprocessor.

Converts Vision detector output into model-ready tensors.
"""

from __future__ import annotations

import cv2
import numpy as np
import tensorflow as tf

from vision.models import Landmark


class Preprocessor:
    """
    Converts Vision outputs into model inputs.
    """

    def __init__(
        self,
        image_size: tuple[int, int] = (224, 224),
    ):

        self.image_size = image_size

    # =====================================================
    # Image
    # =====================================================

    def preprocess_image(
        self,
        image: np.ndarray,
    ) -> np.ndarray:
        """
        Resize and normalize image.
        """

        image = cv2.resize(
            image,
            self.image_size,
        )

        image = image.astype(
            np.float32,
        )

        image /= 255.0

        return image

    # =====================================================
    # Landmarks
    # =====================================================

    @staticmethod
    def preprocess_landmarks(
        landmarks: list[Landmark],
    ) -> np.ndarray:
        """
        Convert Landmark objects into a (63,) float32 vector.

        Output format:
        [x1,y1,z1,x2,y2,z2,...,x21,y21,z21]
        """

        if len(landmarks) != 21:

            raise ValueError(
                f"Expected 21 landmarks, got {len(landmarks)}."
            )

        values = []

        for landmark in landmarks:

            values.extend(
                [
                    landmark.x,
                    landmark.y,
                    landmark.z,
                ]
            )

        values = np.asarray(
            values,
            dtype=np.float32,
        )

        if values.shape != (63,):

            raise ValueError(
                f"Expected landmark vector of shape (63,), got {values.shape}."
            )

        return values

    # =====================================================
    # Model Input
    # =====================================================

    def preprocess(
        self,
        image: np.ndarray,
        landmarks: np.ndarray,
    ) -> dict:
        """
        Build model-ready input dictionary.
        """

        image = self.preprocess_image(
            image,
        )

        landmarks = self.preprocess_landmarks(
            landmarks,
        )

        return {

            "image": tf.expand_dims(
                image,
                axis=0,
            ),

            "landmarks": tf.expand_dims(
                landmarks,
                axis=0,
            ),

        }