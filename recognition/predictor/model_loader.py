"""
Model Loader.

Loads trained GestureRecognitionModel weights.
"""

from __future__ import annotations

from pathlib import Path
from recognition.network import GestureRecognitionModel
import tensorflow as tf


class ModelLoader:
    """
    Loads a trained gesture recognition model.
    """

    def __init__(
        self,
        num_classes: int,
    ):

        self.num_classes = num_classes

    # =====================================================
    # Public API
    # =====================================================

    def load(
        self,
        checkpoint_path: str | Path,
    ) -> GestureRecognitionModel:

        checkpoint_path = Path(checkpoint_path)

        if not checkpoint_path.exists():
            raise FileNotFoundError(
                f"Checkpoint not found: {checkpoint_path}"
            )

        model = GestureRecognitionModel.build_model(
            num_classes=self.num_classes,
        )

        model.load_weights(str(checkpoint_path))

        return model