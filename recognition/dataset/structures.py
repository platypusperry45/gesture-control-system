"""
Data models for the Dataset Builder.

These models represent the cleaned dataset that will be used
throughout the ML pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import numpy as np


# ==========================================================
# One Dataset Sample
# ==========================================================

@dataclass(slots=True)
class Sample:
    """
    One cleaned training sample.
    """

    # -----------------------------
    # Image
    # -----------------------------

    image_path: Path

    # -----------------------------
    # Label Information
    # -----------------------------

    gesture: str

    label: int

    handedness: str

    # -----------------------------
    # Features
    # -----------------------------

    landmarks: np.ndarray = field(
        repr=False,
    )

    # -----------------------------
    # Optional Future Fields
    # -----------------------------

    confidence: float | None = None

    metadata: dict = field(
        default_factory=dict,
        repr=False,
    )

    # -----------------------------
    # Convenience Properties
    # -----------------------------

    @property
    def filename(self) -> str:

        return self.image_path.name

    @property
    def stem(self) -> str:

        return self.image_path.stem

@dataclass(slots=True)
class RawSampleRecord:
    """
    Raw data discovered by the scanner.

    The Builder converts this into a Sample.
    """

    image_path: Path

    gesture: str

    handedness: str

    landmarks: np.ndarray = field(repr=False)

# ==========================================================
# Dataset Split
# ==========================================================

@dataclass(slots=True)
class DatasetSplit:
    """
    Represents one split of the dataset.
    """

    name: str

    samples: list[Sample]

    @property
    def size(self) -> int:

        return len(self.samples)

    def __len__(self):

        return len(self.samples)

    def __iter__(self):

        return iter(self.samples)


# ==========================================================
# Complete Dataset
# ==========================================================

@dataclass(slots=True)
class Dataset:
    """
    Entire cleaned dataset before splitting.
    """

    samples: list[Sample]

    @property
    def size(self) -> int:

        return len(self.samples)

    def __len__(self):

        return len(self.samples)

    def __iter__(self):

        return iter(self.samples)

    def gestures(self) -> list[str]:

        return sorted({

            sample.gesture

            for sample in self.samples

        })

    def class_counts(self) -> dict[str, int]:

        counts = {}

        for sample in self.samples:

            counts[sample.gesture] = (
                counts.get(sample.gesture, 0) + 1
            )

        return counts


# ==========================================================
# Train / Validation / Test
# ==========================================================

@dataclass(slots=True)
class DatasetBundle:
    """
    Final dataset returned by the builder.
    """

    train: DatasetSplit

    validation: DatasetSplit

    test: DatasetSplit

    @property
    def total_size(self) -> int:

        return (

            self.train.size +

            self.validation.size +

            self.test.size

        )