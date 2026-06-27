import cv2

from vision.camera import Camera
from vision.config import VisionConfig
from vision.detector import MediaPipeHandDetector
from vision.preprocess import convert_bgr_to_rgb
from vision.cropper import HandCropper

config = VisionConfig()

camera = Camera(config)
camera.open()

detector = MediaPipeHandDetector(config)
cropper = HandCropper(config)

try:

    while True:

        frame = camera.read()

        rgb = convert_bgr_to_rgb(frame)

        hands = detector.detect(rgb)

        for i, hand in enumerate(hands):

            crop = cropper.crop(
                rgb,
                hand.bounding_box,
            )

            cv2.imshow(
                f"Hand {i}",
                cv2.cvtColor(crop, cv2.COLOR_RGB2BGR),
            )

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == 27:
            break

finally:

    detector.close()
    camera.release()
    cv2.destroyAllWindows()