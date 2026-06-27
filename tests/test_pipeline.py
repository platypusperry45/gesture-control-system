import numpy as np

from vision.pipeline import VisionPipeline
from vision.config import VisionConfig


def test_pipeline_creation():

    pipeline = VisionPipeline(
        VisionConfig()
    )

    frame = np.zeros(
        (480, 640, 3),
        dtype=np.uint8,
    )

    result = pipeline.process(frame)

    assert result.frame.shape == frame.shape

    assert isinstance(result.hands, list)

    pipeline.close()