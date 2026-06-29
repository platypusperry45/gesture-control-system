"""
Augmentation Pipeline.

Applies random augmentations to an image during training.
"""

from __future__ import annotations

import random

import numpy as np

from .config import AugmentationConfig
from . import transforms


class Augmenter:
    """
    On-the-fly image augmentation pipeline.
    """

    def __init__(
        self,
        config: AugmentationConfig | None = None,
    ):

        self.config = (
            config
            if config is not None
            else AugmentationConfig()
        )

    # =====================================================
    # Public API
    # =====================================================

    def __call__(
        self,
        image: np.ndarray,
    ) -> np.ndarray:

        return self.apply(image)

    # =====================================================
    # Main Pipeline
    # =====================================================

    def apply(
        self,
        image: np.ndarray,
    ) -> np.ndarray:

        if not self.config.enabled:

            return transforms.resize(
                image,
                self.config,
            )

        augmented = image.copy()

        # ---------------------------------------------
        # Geometry
        # ---------------------------------------------

        if self._chance(
            self.config.rotation_probability
        ):

            augmented = transforms.rotate(
                augmented,
                self.config,
            )

        if self._chance(
            self.config.translation_probability
        ):

            augmented = transforms.translate(
                augmented,
                self.config,
            )

        if self._chance(
            self.config.scaling_probability
        ):

            augmented = transforms.scale(
                augmented,
                self.config,
            )

        if self._chance(
            self.config.perspective_probability
        ):

            augmented = transforms.perspective(
                augmented,
                self.config,
            )

        # ---------------------------------------------
        # Lighting
        # ---------------------------------------------

        if self._chance(
            self.config.brightness_probability
        ):

            augmented = transforms.brightness(
                augmented,
                self.config,
            )

        if self._chance(
            self.config.contrast_probability
        ):

            augmented = transforms.contrast(
                augmented,
                self.config,
            )

        if self._chance(
            self.config.gamma_probability
        ):

            augmented = transforms.gamma(
                augmented,
                self.config,
            )

        if self._chance(
            self.config.shadow_probability
        ):

            augmented = transforms.shadow(
                augmented,
                self.config,
            )

        # ---------------------------------------------
        # Camera Effects
        # ---------------------------------------------

        if self._chance(
            self.config.noise_probability
        ):

            augmented = transforms.gaussian_noise(
                augmented,
                self.config,
            )

        if self._chance(
            self.config.blur_probability
        ):

            augmented = transforms.motion_blur(
                augmented,
                self.config,
            )

        # ---------------------------------------------
        # Optional Flip
        # ---------------------------------------------

        if self._chance(
            self.config.horizontal_flip_probability
        ):

            augmented = transforms.horizontal_flip(
                augmented,
                self.config,
            )

        # ---------------------------------------------
        # Final Resize
        # ---------------------------------------------

        augmented = transforms.resize(
            augmented,
            self.config,
        )

        # ---------------------------------------------
        # Safety: Always return uint8
        # ---------------------------------------------

        if augmented.dtype != np.uint8:

            augmented = np.clip(
                augmented,
                0,
                255,
            ).astype(np.uint8)

        return augmented

    # =====================================================
    # Helpers
    # =====================================================

    @staticmethod
    def _chance(
        probability: float,
    ) -> bool:

        return random.random() < probability