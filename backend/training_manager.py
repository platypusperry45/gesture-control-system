import threading
from datetime import datetime


class TrainingManager:

    def __init__(self):

        self.lock = threading.Lock()

        self.reset()

    # --------------------------------------------------
    # Reset
    # --------------------------------------------------

    def reset(self):

        with self.lock:

            self.running = False
            self.paused = False
            self.stop_requested = False
            self.completed = False
            self.error = None

            self.epoch = 0
            self.total_epochs = 0

            self.loss = 0.0
            self.val_loss = 0.0

            self.accuracy = 0.0
            self.val_accuracy = 0.0

            self.progress = 0

            self.logs = []

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    def add_log(self, message):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.logs.append({

            "time": timestamp,

            "level": "INFO",

            "message": message,

        })

        if len(self.logs) > 500:

            self.logs = self.logs[-500:]

    # --------------------------------------------------
    # Epoch Update
    # --------------------------------------------------

    def update(

        self,

        epoch,

        total_epochs,

        loss,

        accuracy,

        val_loss=0,

        val_accuracy=0,

    ):

        with self.lock:

            self.epoch = epoch

            self.total_epochs = total_epochs

            self.loss = float(loss)

            self.accuracy = float(accuracy)

            self.val_loss = float(val_loss)

            self.val_accuracy = float(val_accuracy)

            if total_epochs > 0:

                self.progress = int(

                    epoch * 100 / total_epochs

                )

    # --------------------------------------------------
    # Controls
    # --------------------------------------------------

    def request_stop(self):

        self.stop_requested = True

        self.running = False

        self.add_log("Training stop requested.")

    def pause(self):

        self.paused = True

        self.running = False

        self.add_log("Training paused.")

    def resume(self):

        self.paused = False

        self.running = True

        self.add_log("Training resumed.")

    # --------------------------------------------------
    # Status
    # --------------------------------------------------

    def get_status(self):

        return {

            "running": self.running,

            "paused": self.paused,

            "completed": self.completed,

            "stop_requested": self.stop_requested,

            "epoch": self.epoch,

            "total_epochs": self.total_epochs,

            "loss": self.loss,

            "val_loss": self.val_loss,

            "accuracy": self.accuracy,

            "val_accuracy": self.val_accuracy,

            "progress": self.progress,

            "logs": self.logs,

            "error": self.error,

        }