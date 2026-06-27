import cv2

from vision import (
    Camera,
    VisionConfig,
    VisionPipeline,
    draw_features,
)

config = VisionConfig()

camera = Camera(config)
camera.open()

pipeline = VisionPipeline(config)

try:

    while True:

        frame = camera.read()

        result = pipeline.process(frame)

        annotated = draw_features(
            result.frame,
            result,
            config,
        )

        cv2.imshow(
            "Gesture Vision Pipeline",
            annotated,
        )

        for i, hand in enumerate(result.hands):

            cv2.imshow(
                f"Crop {i}",
                cv2.cvtColor(
                    hand.cropped_image,
                    cv2.COLOR_RGB2BGR,
                ),
            )

        if cv2.waitKey(1) == 27:
            break

finally:

    pipeline.close()
    camera.release()

    cv2.destroyAllWindows()