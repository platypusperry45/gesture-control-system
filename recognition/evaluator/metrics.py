"""
Evaluation Metrics.

Provides commonly used evaluation metrics
for gesture recognition.
"""

from __future__ import annotations

import tensorflow as tf


class EvaluationMetrics:
    """
    Factory for evaluation metrics.
    """

    # =====================================================
    # Accuracy
    # =====================================================

    @staticmethod
    def accuracy():

        return tf.keras.metrics.SparseCategoricalAccuracy(
            name="accuracy",
        )

    # =====================================================
    # Top-K Accuracy
    # =====================================================

    @staticmethod
    def top_k_accuracy(
        k: int = 3,
    ):

        return tf.keras.metrics.SparseTopKCategoricalAccuracy(
            k=k,
            name=f"top_{k}_accuracy",
        )

    # =====================================================
    # Metric Collection
    # =====================================================

    @classmethod
    def build(
        cls,
    ) -> list[tf.keras.metrics.Metric]:

        return [

            cls.accuracy(),

            cls.top_k_accuracy(),

        ]