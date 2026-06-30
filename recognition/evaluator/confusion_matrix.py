"""
Confusion Matrix utilities.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import confusion_matrix


class ConfusionMatrix:
    """
    Utilities for confusion matrix generation
    and visualization.
    """

    # =====================================================
    # Compute
    # =====================================================

    @staticmethod
    def compute(
        y_true,
        y_pred,
        normalize: bool = False,
    ) -> np.ndarray:

        mode = "true" if normalize else None

        return confusion_matrix(
            y_true,
            y_pred,
            normalize=mode,
        )

    