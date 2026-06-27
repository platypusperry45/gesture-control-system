import cv2

from vision.preprocess import (
    mirror_frame,
    convert_bgr_to_rgb
)

cap = cv2.VideoCapture(0)

while True:

    ret, frame = cap.read()

    if not ret:
        break

    mirrored = mirror_frame(frame)

    rgb = convert_bgr_to_rgb(mirrored)

    # Convert back only for displaying
    bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)

    cv2.imshow("Preprocess Demo", bgr)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()