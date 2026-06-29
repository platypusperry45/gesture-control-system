"""
Dataset Splitter.

Creates reproducible train / validation / test splits while
preserving class balance.
"""

from __future__ import annotations

import random
from collections import defaultdict

from .models import (
    Dataset,
    DatasetBundle,
    DatasetSplit,
    Sample,
)


class DatasetSplitter:
    """
    Stratified dataset splitter.
    """

    def __init__(
        self,
        train_ratio: float = 0.70,
        validation_ratio: float = 0.15,
        test_ratio: float = 0.15,
        random_seed: int = 42,
    ):

        total = (
            train_ratio
            + validation_ratio
            + test_ratio
        )

        if abs(total - 1.0) > 1e-6:
            raise ValueError(
                "Split ratios must sum to 1."
            )

        self.train_ratio = train_ratio
        self.validation_ratio = validation_ratio
        self.test_ratio = test_ratio

        self.random_seed = random_seed

    # =====================================================
    # Public API
    # =====================================================

    def split(
        self,
        dataset: Dataset,
    ) -> DatasetBundle:

        grouped = self._group_by_gesture(
            dataset.samples
        )

        train = []
        validation = []
        test = []

        rng = random.Random(
            self.random_seed
        )

        for samples in grouped.values():

            samples = samples.copy()

            rng.shuffle(samples)

            n = len(samples)

            train_end = int(
                n * self.train_ratio
            )

            validation_end = (
                train_end +
                int(
                    n *
                    self.validation_ratio
                )
            )

            train.extend(
                samples[:train_end]
            )

            validation.extend(
                samples[
                    train_end:validation_end
                ]
            )

            test.extend(
                samples[
                    validation_end:
                ]
            )

        rng.shuffle(train)
        rng.shuffle(validation)
        rng.shuffle(test)

        return DatasetBundle(

            train=DatasetSplit(
                name="train",
                samples=train,
            ),

            validation=DatasetSplit(
                name="validation",
                samples=validation,
            ),

            test=DatasetSplit(
                name="test",
                samples=test,
            ),

        )

    # =====================================================
    # Helpers
    # =====================================================

    @staticmethod
    def _group_by_gesture(
        samples: list[Sample],
    ) -> dict[str, list[Sample]]:

        grouped = defaultdict(list)

        for sample in samples:

            grouped[
                sample.gesture
            ].append(sample)

        return grouped