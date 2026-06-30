"""
Dataset Builder.

Converts RawSampleRecords into Sample objects.
"""

from __future__ import annotations
import numpy as np
from .label_encoder import LabelEncoder
from .models import (
    Dataset,
    Sample,
)
from .scanner import DatasetScanner

from recognition.config import GESTURES


class DatasetBuilder:
    """
    Builds a clean Dataset from the raw files.
    """

    def __init__(self):

        self.scanner = DatasetScanner()

        self.encoder = LabelEncoder(
            GESTURES
        )
    @property
    def label_encoder(self):
        return self.encoder
    
    # =====================================================
    # Public API
    # =====================================================

    def build(self) -> Dataset:

        raw_records = self.scanner.scan()

        samples = [

            self._build_sample(record)

            for record in raw_records

        ]

        return Dataset(samples)

    # =====================================================
    # Helpers
    # =====================================================

    def _build_sample(
        self,
        record,
    ) -> Sample:

        row = record.landmark_row

        handedness = row[1]

        landmarks = np.asarray(
            row[2:],
            dtype=np.float32,
        )

        return Sample(

            image_path=record.image_path,

            gesture=record.gesture,

            label=self.encoder.encode(
                record.gesture,
            ),

            handedness=handedness,

            landmarks=landmarks,

        )