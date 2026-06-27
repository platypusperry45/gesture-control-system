import cv2

from vision.camera import Camera
from vision.config import VisionConfig


config = VisionConfig()

with Camera(config) as camera:

    while True:

        frame = camera.read()

        cv2.imshow("Camera Test", frame)

        if cv2.waitKey(1) == 27:
            break

cv2.destroyAllWindows()