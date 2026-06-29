"""
Label Encoder.

Provides a consistent mapping between gesture names and
integer class labels.
"""

from __future__ import annotations

from typing import Iterable


class LabelEncoder:
    """
    Bidirectional mapping between gesture names and labels.
    """

    def __init__(
        self,
        gestures: Iterable[str],
    ):

        gestures = list(gestures)

        if len(gestures) == 0:
            raise ValueError(
                "At least one gesture is required."
            )

        if len(set(gestures)) != len(gestures):
            raise ValueError(
                "Duplicate gesture names detected."
            )

        self._gestures = list(gestures)

        self._gesture_to_label = {

            gesture: index

            for index, gesture in enumerate(
                self._gestures
            )

        }

        self._label_to_gesture = {

            index: gesture

            for gesture, index in
            self._gesture_to_label.items()

        }

    # -------------------------------------------------
    # Encode
    # -------------------------------------------------

    def encode(
        self,
        gesture: str,
    ) -> int:

        if gesture not in self._gesture_to_label:

            raise KeyError(
                f"Unknown gesture: {gesture}"
            )

        return self._gesture_to_label[gesture]

    # -------------------------------------------------
    # Decode
    # -------------------------------------------------

    def decode(
        self,
        label: int,
    ) -> str:

        if label not in self._label_to_gesture:

            raise KeyError(
                f"Unknown label: {label}"
            )

        return self._label_to_gesture[label]

    # -------------------------------------------------
    # Helpers
    # -------------------------------------------------

    @property
    def classes(self) -> list[str]:

        return self._gestures.copy()

    @property
    def num_classes(self) -> int:

        return len(self._gestures)

    def __len__(self):

        return len(self._gestures)

    def __contains__(
        self,
        gesture: str,
    ):

        return gesture in self._gesture_to_label

    def __repr__(self):

        return (
            f"LabelEncoder("
            f"{self.num_classes} classes)"
        )