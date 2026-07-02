from pathlib import Path

from recognition.predictor.inference import InferenceEngine
from recognition.config import GESTURES

MODEL_PATH = Path(
    "recognition/artifacts/trained_models/gesture_recognition.weights.h5"
)

engine = InferenceEngine(
    checkpoint_path=MODEL_PATH,
    class_names=GESTURES,
    camera_source=0,
)

engine.run()