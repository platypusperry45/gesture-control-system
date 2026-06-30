"""
Visualization utilities.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


class Visualization:
    """
    Visualization utilities for training
    and evaluation.
    """

    # =====================================================
    # Save Figure
    # =====================================================

    @staticmethod
    def _save_figure(
        save_path: str | Path | None,
    ):

        if save_path is None:
            return

        save_path = Path(save_path)

        save_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        plt.savefig(
            save_path,
            dpi=300,
            bbox_inches="tight",
        )

    # =====================================================
    # Confusion Matrix
    # =====================================================

    @staticmethod
    def plot_confusion_matrix(
        matrix: np.ndarray,
        class_names: list[str],
        *,
        title: str = "Confusion Matrix",
        save_path: str | Path | None = None,
        figsize: tuple[int, int] = (8, 8),
    ):

        fig = plt.figure(figsize=figsize)

        plt.imshow(
            matrix,
            interpolation="nearest",
        )

        plt.title(title)

        plt.colorbar()

        ticks = np.arange(
            len(class_names)
        )

        plt.xticks(
            ticks,
            class_names,
            rotation=45,
            ha="right",
        )

        plt.yticks(
            ticks,
            class_names,
        )

        plt.xlabel(
            "Predicted Label"
        )

        plt.ylabel(
            "True Label"
        )

        threshold = matrix.max() / 2

        for i in range(matrix.shape[0]):

            for j in range(matrix.shape[1]):

                value = matrix[i, j]

                if isinstance(
                    value,
                    np.floating,
                ):
                    text = f"{value:.2f}"
                else:
                    text = str(value)

                plt.text(
                    j,
                    i,
                    text,
                    ha="center",
                    va="center",
                    color=(
                        "white"
                        if value > threshold
                        else "black"
                    ),
                )

        plt.tight_layout()

        Visualization._save_figure(
            save_path,
        )

        return fig

    # =====================================================
    # Training Curves
    # =====================================================

    @staticmethod
    def plot_history(
        history,
        *,
        save_path: str | Path | None = None,
    ):

        history = history.history

        fig = plt.figure(
            figsize=(10, 5)
        )

        # Loss

        plt.subplot(
            1,
            2,
            1,
        )

        plt.plot(
            history["loss"],
            label="Train",
        )

        if "val_loss" in history:

            plt.plot(
                history["val_loss"],
                label="Validation",
            )

        plt.title("Loss")

        plt.xlabel("Epoch")

        plt.legend()

        # Accuracy

        plt.subplot(
            1,
            2,
            2,
        )

        if "accuracy" in history:

            plt.plot(
                history["accuracy"],
                label="Train",
            )

        if "val_accuracy" in history:

            plt.plot(
                history["val_accuracy"],
                label="Validation",
            )

        plt.title("Accuracy")

        plt.xlabel("Epoch")

        plt.legend()

        plt.tight_layout()

        Visualization._save_figure(
            save_path,
        )

        return fig

    # =====================================================
    # Class Distribution
    # =====================================================

    @staticmethod
    def plot_class_distribution(
        class_counts: dict[str, int],
        *,
        save_path: str | Path | None = None,
    ):

        fig = plt.figure(
            figsize=(10, 5)
        )

        names = list(
            class_counts.keys()
        )

        counts = list(
            class_counts.values()
        )

        plt.bar(
            names,
            counts,
        )

        plt.xticks(
            rotation=45,
            ha="right",
        )

        plt.ylabel(
            "Samples"
        )

        plt.title(
            "Class Distribution"
        )

        plt.tight_layout()

        Visualization._save_figure(
            save_path,
        )

        return fig