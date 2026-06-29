"""
Configuration for the complete training pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass


# ==========================================================
# Augmentation
# ==========================================================

@dataclass(slots=True)
class AugmentationConfig:
    """
    Image augmentation configuration.
    """

    enabled: bool = True

    image_size: tuple[int, int] = (224, 224)

    # Geometry
    rotation_probability: float = 0.50
    max_rotation: float = 15.0

    translation_probability: float = 0.30
    max_translation: float = 0.10

    scaling_probability: float = 0.30
    min_scale: float = 0.90
    max_scale: float = 1.10

    perspective_probability: float = 0.20
    perspective_scale: float = 0.08

    horizontal_flip_probability: float = 0.20

    # Lighting
    brightness_probability: float = 0.50
    brightness_delta: float = 25.0

    contrast_probability: float = 0.50
    min_contrast: float = 0.85
    max_contrast: float = 1.15

    gamma_probability: float = 0.20
    min_gamma: float = 0.90
    max_gamma: float = 1.10

    shadow_probability: float = 0.20
    shadow_strength: float = 0.35

    # Camera Effects
    blur_probability: float = 0.20
    max_blur_kernel: int = 7

    noise_probability: float = 0.20
    noise_std: float = 5.0


# ==========================================================
# Training
# ==========================================================

@dataclass(slots=True)
class TrainingConfig:
    """
    Training hyperparameters.
    """

    batch_size: int = 32

    epochs: int = 50

    learning_rate: float = 1e-3

    weight_decay: float = 1e-4

    gradient_clip_norm: float = 1.0

    validation_frequency: int = 1

    shuffle_buffer_size: int = 2048

    random_seed: int = 42


# ==========================================================
# Scheduler
# ==========================================================

@dataclass(slots=True)
class SchedulerConfig:
    """
    Learning-rate scheduler.
    """

    factor: float = 0.5

    patience: int = 5

    min_learning_rate: float = 1e-6


# ==========================================================
# Early Stopping
# ==========================================================

@dataclass(slots=True)
class EarlyStoppingConfig:
    """
    Early stopping configuration.
    """

    monitor: str = "val_loss"

    patience: int = 10

    restore_best_weights: bool = True


# ==========================================================
# Checkpoint
# ==========================================================
@dataclass(slots=True)
class CheckpointConfig:
    """
    Model checkpoint configuration.
    """

    monitor: str = "val_accuracy"

    mode: str = "max"

    save_best_only: bool = True