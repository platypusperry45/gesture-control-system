"""
Configuration for the training augmentation pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class AugmentationConfig:
    """
    Configuration for image augmentation.
    """

    # Enable / Disable
    enabled: bool = True

    # Image size
    resize_height: int = 224
    resize_width: int = 224
    image_size: tuple[int, int] = (224, 224)

    # Rotation
    rotation_probability: float = 0.50
    max_rotation: float = 15.0

    # Translation
    translation_probability: float = 0.30
    max_translation: float = 0.10

    # Scaling
    scaling_probability: float = 0.30
    min_scale: float = 0.90
    max_scale: float = 1.10

    # Perspective
    perspective_probability: float = 0.20
    perspective_scale: float = 0.08

    # Horizontal Flip
    horizontal_flip_probability: float = 0.20

    # Brightness
    brightness_probability: float = 0.50
    brightness_delta: float = 0.15

    # Contrast
    contrast_probability: float = 0.50
    min_contrast: float = 0.85
    max_contrast: float = 1.15

    # Gamma
    gamma_probability: float = 0.20
    min_gamma: float = 0.80
    max_gamma: float = 1.20

    # Blur
    blur_probability: float = 0.20
    max_blur_kernel: int = 3

    # Noise
    noise_probability: float = 0.20
    noise_std: float = 5.0

    # Shadow
    shadow_probability: float = 0.20
    shadow_strength: float = 0.25