import time

from vision.fps import FPSCounter


def test_fps_positive():

    counter = FPSCounter()

    time.sleep(0.01)

    fps = counter.update()

    assert fps > 0


def test_reset():

    counter = FPSCounter()

    time.sleep(0.01)

    counter.update()

    counter.reset()

    assert len(counter.buffer) == 0