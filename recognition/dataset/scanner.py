"""
Dataset Scanner.

Scans the raw dataset and returns RawSampleRecord objects.

Responsibilities
----------------
- Discover image files
- Load landmark CSVs
- Match images with landmarks
- Ignore stale landmark rows
- Ignore stale metadata
"""

from __future__ import annotations
import csv
from pathlib import Path

from recognition.config import (
    GESTURES,
    IMAGE_DIR,
    LANDMARK_DIR,
)

from .models import RawSampleRecord


class DatasetScanner:

    """
    Scans the raw dataset.

    Images are considered the source of truth.
    """

    def __init__(self):

        self._landmark_lookup = {}

    # ======================================================
    # Public API
    # ======================================================

    def scan(self) -> list[RawSampleRecord]:

        self._load_landmarks()

        records = []

        for gesture in GESTURES:

            records.extend(
                self._scan_gesture(
                    gesture,
                )
            )

        return records

    # ======================================================
    # Landmark Loading
    # ======================================================

    def _load_landmarks(self):

        self._landmark_lookup.clear()

        for gesture in GESTURES:

            csv_path = LANDMARK_DIR / f"{gesture}.csv"

            if not csv_path.exists():
                continue

            lookup = {}

            with open(
                csv_path,
                newline="",
                encoding="utf-8",
            ) as file:

                reader = csv.reader(file)

                next(reader, None)

                for row in reader:

                    if not row:
                        continue

                    filename = row[0]

                    lookup[filename] = row

            self._landmark_lookup[
                gesture
            ] = lookup

    # ======================================================
    # Scan One Gesture
    # ======================================================

    def _scan_gesture(
        self,
        gesture: str,
    ) -> list[RawSampleRecord]:

        folder = IMAGE_DIR / gesture

        if not folder.exists():

            return []

        lookup = self._landmark_lookup.get(
            gesture,
            {},
        )

        records = []

        for image_path in sorted(
            folder.glob("*.png")
        ):

            row = lookup.get(
                image_path.name
            )

            # Ignore orphan images
            if row is None:

                continue

            if len(row) != 65:

                continue
            
            records.append(

                RawSampleRecord(

                    image_path=image_path,

                    gesture=gesture,

                    landmark_row=row,

                )

            )
            

        return records