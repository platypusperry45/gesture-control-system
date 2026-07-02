"""
Camera.

Wrapper around OpenCV VideoCapture.
"""

from __future__ import annotations

import cv2
import numpy as np


class Camera:
    """
    Camera wrapper.

    Supports webcams and video files.
    """

    def __init__(
        self,
        source: int | str = 0,
        width: int = 1280,
        height: int = 720,
    ):

        self.capture = cv2.VideoCapture(source)

        if not self.capture.isOpened():

            raise RuntimeError(
                f"Unable to open camera/video: {source}"
            )

        self.capture.set(
            cv2.CAP_PROP_FRAME_WIDTH,
            width,
        )

        self.capture.set(
            cv2.CAP_PROP_FRAME_HEIGHT,
            height,
        )

    # =====================================================
    # Read One Frame
    # =====================================================

    def read(self) -> np.ndarray | None:
        """
        Returns an RGB frame.

        Returns
        -------
        RGB image or None if stream ends.
        """

        success, frame = self.capture.read()

        if not success:

            return None

        return frame

    # =====================================================
    # Window
    # =====================================================

    @staticmethod
    def show(
        window_name: str,
        frame: np.ndarray,
    ) -> None:
        """
        Display an RGB frame.
        """

        cv2.imshow(
            window_name,
            frame,
        )
        

    # =====================================================
    # Keyboard
    # =====================================================

    @staticmethod
    def should_close(
        key: str = "q",
    ) -> bool:
        """
        Returns True if the user pressed the exit key.
        """

        return (

            cv2.waitKey(1) & 0xFF

        ) == ord(key)

    # =====================================================
    # Cleanup
    # =====================================================

    def close(self):

        self.capture.release()

        cv2.destroyAllWindows()