import time

from vision.fps import FPSCounter

counter = FPSCounter()

for _ in range(100):

    time.sleep(0.02)

    print(f"FPS: {counter.update():.2f}")