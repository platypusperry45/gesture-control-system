import cv2

from vision.camera import Camera
from vision.config import VisionConfig
from vision.detector import MediaPipeHandDetector
from vision.preprocess import convert_bgr_to_rgb


config = VisionConfig()

camera = Camera(config)
camera.open()

detector = MediaPipeHandDetector(config)

try:

    while True:

        frame = camera.read()

        rgb = convert_bgr_to_rgb(frame)

        hands = detector.detect(rgb)

        print("-" * 40)
        print(f"Hands detected: {len(hands)}")

        for hand in hands:

            print("Hand:", hand.handedness)
            print("Confidence:", round(hand.confidence, 2))
            print("Bounding Box:", hand.bounding_box)

        cv2.imshow("Camera", frame)

        if cv2.waitKey(1) == 27:
            break

finally:

    detector.close()
    camera.release()
    cv2.destroyAllWindows()