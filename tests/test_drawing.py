import numpy as np

from vision.config import VisionConfig
from vision.drawing import draw_features
from vision.models import FrameResult


def test_draw_empty_frame():

    config = VisionConfig()

    frame = np.zeros(
        (480, 640, 3),
        dtype=np.uint8,
    )

    result = FrameResult(
        frame=frame,
        timestamp=0.0,
        fps=30.0,
        hands=[],
    )

    annotated = draw_features(
        frame,
        result,
        config,
    )

    assert annotated.shape == frame.shape