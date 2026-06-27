"""
Camera handling module for the Vision Layer.
"""

from typing import Optional

import cv2
import numpy as np

from .config import VisionConfig
from .exceptions import CameraUnavailableError, FrameReadError
from .logger import logger


class Camera:
    """
    Handles webcam initialization, frame acquisition,
    and safe resource cleanup.
    """

    def __init__(self, config: VisionConfig):
        self.config = config
        self.cap: Optional[cv2.VideoCapture] = None

    def open(self) -> None:
        """
        Opens the configured camera.
        """

        self.cap = cv2.VideoCapture(self.config.camera_index)

        if not self.cap.isOpened():
            raise CameraUnavailableError(
                f"Unable to open camera {self.config.camera_index}"
            )

        width, height = self.config.resolution

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

        logger.info(
            "Camera opened (%dx%d)",
            width,
            height,
        )

    def read(self) -> np.ndarray:
        """
        Reads one BGR frame.

        Returns
        -------
        np.ndarray
            BGR image.
        """

        if self.cap is None:
            raise CameraUnavailableError("Camera has not been opened.")

        success, frame = self.cap.read()

        if not success:
            raise FrameReadError("Failed to read frame from webcam.")

        return frame

    def release(self) -> None:
        """
        Releases camera resources.
        """

        if self.cap is not None:
            self.cap.release()
            self.cap = None
            logger.info("Camera released.")

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.release()