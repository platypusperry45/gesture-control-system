"""
Preprocessor.

Converts Vision detector output into model-ready tensors.
"""

from __future__ import annotations

import cv2
import numpy as np
import tensorflow as tf


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
        Resize and normalize cropped hand image.
        """
        cv2.imwrite("debug_crop.png", image)
        image = cv2.resize(
            image,
            self.image_size,
            interpolation=cv2.INTER_LINEAR,
        )

        image = image.astype(np.float32)

        image /= 255.0

        return image

    # =====================================================
    # Landmarks
    # =====================================================

    @staticmethod
    def preprocess_landmarks(
        landmarks,
    ) -> np.ndarray:
        """
        Convert landmarks into a normalized (63,) vector.

        Supports:
            - list[Landmark]
            - ndarray (21,3)
            - ndarray (63,)
        """

        # ----------------------------
        # Convert to (21,3)
        # ----------------------------

        if isinstance(landmarks, np.ndarray):

            landmarks = landmarks.astype(np.float32)

            if landmarks.shape == (63,):
                landmarks = landmarks.reshape(21, 3)

            elif landmarks.shape != (21, 3):
                raise ValueError(
                    f"Unsupported landmark shape: {landmarks.shape}"
                )

        else:

            if len(landmarks) != 21:
                raise ValueError(
                    f"Expected 21 landmarks, got {len(landmarks)}."
                )

            landmarks = np.asarray(
                [
                    [lm.x, lm.y, lm.z]
                    for lm in landmarks
                ],
                dtype=np.float32,
            )

        # ----------------------------
        # Translation normalization
        # Wrist becomes origin
        # ----------------------------

        wrist = landmarks[0].copy()

        landmarks = landmarks - wrist

        # ----------------------------
        # Scale normalization
        # ----------------------------

        distances = np.linalg.norm(
            landmarks[:, :2],
            axis=1,
        )

        scale = np.max(distances)

        if scale > 1e-6:
            landmarks /= scale

        return landmarks.reshape(63).astype(np.float32)

    # =====================================================
    # Model Input
    # =====================================================

    def preprocess(
        self,
        image: np.ndarray,
        landmarks,
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
            "image": tf.convert_to_tensor(
                image[np.newaxis, ...],
                dtype=tf.float32,
            ),
            "landmarks": tf.convert_to_tensor(
                landmarks[np.newaxis, ...],
                dtype=tf.float32,
            ),
        }