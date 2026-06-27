from vision.models import Landmark
from vision.utils import (
    calculate_bounding_box,
    calculate_hand_center,
)

landmarks = [
    Landmark(0, 0.2, 0.2, 0),
    Landmark(1, 0.8, 0.8, 0),
]

bbox = calculate_bounding_box(
    landmarks,
    640,
    480,
)

center = calculate_hand_center(bbox)

print("Bounding Box:", bbox)
print("Center:", center)