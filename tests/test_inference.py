import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from recognition.predictor.inference import InferenceEngine

engine = InferenceEngine(
    checkpoint_path="path/to/model.h5",
    class_names=["class1", "class2", "class3"],
    camera_source=0
)

engine.run()