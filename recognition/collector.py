"""
Gesture Dataset Collector.

Responsibilities
----------------
- Camera management
- Vision pipeline execution
- User interaction
- Dataset collection UI

Storage is delegated to DatasetStorage.
"""

from __future__ import annotations

import time
import numpy as np
import cv2

from vision import (
    Camera,
    VisionConfig,
    VisionPipeline,
)

from .config import (
    GESTURES,
    WINDOW_NAME,
    CROP_WINDOW_NAME,
    SHOW_HAND_CROP,
    SHOW_FPS,
    SHOW_CONFIDENCE,

    COUNTDOWN_SECONDS,
    AUTO_CAPTURE_FPS,
    TARGET_SAMPLES_PER_GESTURE,
    AUTO_SWITCH_GESTURE,
    SHOW_PROGRESS_BAR,
    SHOW_STATUS,
    SAMPLES_PER_SESSION,
)

from .storage import DatasetStorage

from .quality import QualityFilter

class DatasetCollector:
    """
    Interactive gesture dataset collector.
    """

    def __init__(self):

        # ----------------------------------------
        # Vision Layer
        # ----------------------------------------

        self.config = VisionConfig()

        self.camera = Camera(self.config)

        self.pipeline = VisionPipeline(self.config)

        # ----------------------------------------
        # Storage Layer
        # ----------------------------------------

        self.storage = DatasetStorage()


        self.quality = QualityFilter()


        # ----------------------------------------
        # Session State
        # ----------------------------------------

        self.current_gesture_index = 0

        self.session_samples = 0

        self.start_time = time.time()

        # -----------------------------
        # Collection State
        # -----------------------------

        self.collection_mode = False

        self.countdown_active = False

        self.countdown_start = 0.0

        self.last_capture_time = 0.0

        self.current_target = TARGET_SAMPLES_PER_GESTURE
        
        self.session_target = SAMPLES_PER_SESSION

        self.session_collected = 0

        self.status = "READY"
         
        self.last_quality = "GOOD"

        # ---------------------------------------
        # Quality Statistics
        # ---------------------------------------

        self.saved_samples = 0

        self.rejected_samples = 0

        self.rejection_stats = {
            "LOW CONFIDENCE": 0,
            "HAND TOO SMALL": 0,
            "CROP TOO SMALL": 0,
            "HAND OUTSIDE FRAME": 0,
        }

        print()

        print("=" * 60)

        print(" Gesture Dataset Collector ")

        print("=" * 60)

        print()

        print("Controls")

        print(" S   Save Sample")

        print(" N   Next Gesture")

        print(" ESC Exit")

        print()

    # ---------------------------------------------------------
    # Properties
    # ---------------------------------------------------------

    @property
    def current_gesture(self) -> str:

        return GESTURES[self.current_gesture_index]

    # ---------------------------------------------------------
    # Main Loop
    # ---------------------------------------------------------

    def run(self):

        self.camera.open()

        try:

            while True:

                frame = self.camera.read()

                result = self.pipeline.process(frame)

                # Update countdown state
                self._update_countdown()

                # Process automatic collection
                if self.collection_mode:
                    self._update_collection(result)

                # Draw UI
                self._process_frame(result)

                # Keyboard
                if not self._handle_keyboard(result):
                    break

        finally:

            self._cleanup()

    # ---------------------------------------------------------
    # Cleanup
    # ---------------------------------------------------------

    def _cleanup(self):

        print()

        print("Closing Dataset Collector...")

        self.pipeline.close()

        self.camera.release()

        cv2.destroyAllWindows()

        print("Done.")

        # ---------------------------------------------------------
    # Frame Processing
    # ---------------------------------------------------------

    def _process_frame(self, result):

        display = result.frame.copy()

        self._draw_overlay(
            display,
            result,
        )

        cv2.imshow(
            WINDOW_NAME,
            display,
        )

        self._show_crop(result)

    # ---------------------------------------------------------
    # Overlay Drawing
    # ---------------------------------------------------------

    def _draw_overlay(
        self,
        frame,
        result,
    ):

        elapsed = int(
            time.time() - self.start_time
        )

        minutes = elapsed // 60

        seconds = elapsed % 60

        y = 35

        cv2.putText(
            frame,
            f"Gesture : {self.current_gesture}",
            (15, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2,
        )

        y += 35

        cv2.putText(
            frame,
            f"Saved : {self.session_samples}",
            (15, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (255, 255, 0),
            2,
        )
        
        y += 35

        cv2.putText(
            frame,
            f"Session : {self.session_collected}/{self.session_target}",
            (15, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 200, 255),
            2,
        )

        y += 35

        cv2.putText(
            frame,
            f"Status : {self.status}",
            (15, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 0),
            2,
        )

        y += 35

        quality_color = (
            (0, 255, 0)
            if self.last_quality == "GOOD"
            else (0, 0, 255)
        )

        cv2.putText(
            frame,
            f"Quality : {self.last_quality}",
            (15, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            quality_color,
            2,
        )

        y += 35

        cv2.putText(
            frame,
            f"Accepted : {self.saved_samples}",
            (15, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 255, 0),
            2,
        )

        y += 35

        cv2.putText(
            frame,
            f"Rejected : {self.rejected_samples}",
            (15, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (0, 0, 255),
            2,
        )

        y += 35

        if SHOW_FPS:

            cv2.putText(
                frame,
                f"FPS : {result.fps:.1f}",
                (15, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (0, 255, 255),
                2,
            )

            y += 35

        if SHOW_CONFIDENCE:

            confidence = 0.0

            handedness = "-"

            if result.hands:

                confidence = result.hands[0].confidence

                handedness = result.hands[0].handedness

            cv2.putText(
                frame,
                f"Hand : {handedness}",
                (15, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (255, 200, 0),
                2,
            )

            y += 35

            cv2.putText(
                frame,
                f"Confidence : {confidence:.2f}",
                (15, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (255, 200, 0),
                2,
            )

            y += 35

        cv2.putText(
            frame,
            f"Time : {minutes:02d}:{seconds:02d}",
            (15, y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.75,
            (255, 255, 255),
            2,
        )

        controls = (
          "[SPACE] Collect   "
          "[S] Save   "
          "[N] Next Gesture   "
          "[ESC] Exit"
        )

        text_size, _ = cv2.getTextSize(
            controls,
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            2,
        )

        cv2.rectangle(
            frame,
            (10, frame.shape[0] - 40),
            (20 + text_size[0], frame.shape[0] - 5),
            (40, 40, 40),
            -1,
        )

        cv2.putText(
            frame,
            controls,
            (15, frame.shape[0] - 15),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (255, 255, 255),
            2,
        )

        if self.countdown_active:

            elapsed = time.time() - self.countdown_start

            remaining = max(
            0,
            COUNTDOWN_SECONDS - int(elapsed),
            )

            text = str(remaining)

            size = cv2.getTextSize(
                text,
                cv2.FONT_HERSHEY_SIMPLEX,
                4,
                6,
            )[0]

            x = (frame.shape[1] - size[0]) // 2

            y = (frame.shape[0] + size[1]) // 2

            cv2.putText(
                frame,
                text,
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                4,
                (0, 0, 255),
                6,
            )
    # ---------------------------------------------------------
    # Hand Crop Window
    # ---------------------------------------------------------

    def _show_crop(
        self,
        result,
    ):

        if not SHOW_HAND_CROP:

            return

        if not result.hands:
  
            blank = np.full(
                (300, 300, 3),
                255,
                dtype=np.uint8,               
            )

            cv2.putText(
                blank,
                "No Hand Detected",
                (35, 150),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 0, 255),
                2,
            )

            cv2.imshow(
                CROP_WINDOW_NAME,
                blank,
            )
            return

        crop = cv2.cvtColor(
            result.hands[0].cropped_image,
            cv2.COLOR_RGB2BGR,
        )

        cv2.imshow(
            CROP_WINDOW_NAME,
            crop,
        )

    # ---------------------------------------------------------
    # Keyboard Handling
    # ---------------------------------------------------------

    def _handle_keyboard(
        self,
        result,
    ) -> bool:

        key = cv2.waitKey(1) & 0xFF

        # ESC
        if key == 27:
            return False

        # SPACE
        elif key == 32:

            if (
                not self.collection_mode
                and not self.countdown_active
            ):
                self._start_countdown()

        # Manual Save
        elif key == ord("s"):

            if result.hands:

                self._save_current_hand(
                    result.hands[0]
                )

            else:

                print("No hand detected.")

    # Next Gesture
        elif key == ord("n"):

            self._next_gesture()

        return True

    # ---------------------------------------------------------
    # Save Current Hand
    # ---------------------------------------------------------

    def _save_current_hand(
        self,
        hand,
    ):

        filename = self.storage.save_sample(
            hand,
            self.current_gesture,
        )

        self.session_samples += 1

        gesture_total = self.storage.get_sample_count(
            self.current_gesture,
        )

        print(
            f"[{self.current_gesture}] "
            f"{filename} saved "
            f"({gesture_total}/{self.current_target})"
        )

    # ---------------------------------------------------------
    # Next Gesture
    # ---------------------------------------------------------

    def _next_gesture(self):

        self.current_gesture_index = (
            self.current_gesture_index + 1
        ) % len(GESTURES)

        print()

        print(
            f"Current Gesture → "
            f"{self.current_gesture}"
        )

        print()

    # ---------------------------------------------------------
    # Countdown
    # ---------------------------------------------------------

    def _start_countdown(self):

        self.countdown_active = True

        self.countdown_start = time.time()

        self.status = "COUNTDOWN"

        print()

        print("Countdown started...")

    def _update_countdown(self):

        if not self.countdown_active:
           return

        elapsed = time.time() - self.countdown_start

        if elapsed >= COUNTDOWN_SECONDS:

            self.countdown_active = False

            self._start_collection()

    def _start_collection(self):

        self.collection_mode = True

        self.last_capture_time = time.time()

        self.session_collected = 0

        self.status = "COLLECTING"

        print()

        print(
            f"Collecting "
            f"{self.session_target} samples..."
        )
    def _update_collection(
        self,
        result,
    ):

        if not self.collection_mode:
            return

        if not result.hands:
            return

        interval = 1.0 / AUTO_CAPTURE_FPS

        current_time = time.time()

        if (
            current_time - self.last_capture_time
            < interval
        ):
           return

        self.last_capture_time = current_time

        report = self.quality.evaluate(
            result.hands[0],
            result.frame.shape,
        )
        
        self.last_quality = report.reason

        if report.valid:

         self.saved_samples += 1

         self._save_current_hand(
          result.hands[0]
        )

        else:

            self.rejected_samples += 1

            if report.reason in self.rejection_stats:

                self.rejection_stats[
                report.reason
            ] += 1

            return

        self.session_collected += 1

        if (
            self.session_collected
            >= self.session_target
        ):
            self._finish_collection()

    def _finish_collection(self):

        self.collection_mode = False

        self.status = "READY"

        print()

        print(
            f"Session Complete "
            f"({self.session_collected} samples)"
        )

        print()

def main():

    collector = DatasetCollector()

    collector.run()


if __name__ == "__main__":

    main()