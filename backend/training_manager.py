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

            self.history = []

            self.started_at = None
            self.finished_at = None

            self.training_time = 0.0

            self.best_accuracy = 0.0
            self.best_val_accuracy = 0.0
            self.test_loss = 0.0
            self.test_accuracy = 0.0

            self.dataset_size = 0
            self.num_classes = 0
            self.class_names = []
            
    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    def add_log(self, message, level="INFO"):

        timestamp = datetime.now().strftime("%H:%M:%S")

        self.logs.append(
            {
                "time": timestamp,
                "level": level,
                "message": message,
            }
        )

        if len(self.logs) > 500:
            self.logs = self.logs[-500:]

    # --------------------------------------------------
    # Training Lifecycle
    # --------------------------------------------------

    def start(self):

        with self.lock:

            self.running = True
            self.completed = False
            self.stop_requested = False
            self.error = None

            self.started_at = datetime.now()
            self.finished_at = None
            self.training_time = 0.0

            self.logs.clear()
            self.history.clear()

            self.add_log("Training started.")

    def finish(self):

        with self.lock:

            self.running = False
            self.completed = True

            self.finished_at = datetime.now()

            if self.started_at:
                self.training_time = (
                    self.finished_at - self.started_at
                ).total_seconds()

            self.add_log("Training completed successfully.")

    # --------------------------------------------------
    # Epoch Updates
    # --------------------------------------------------

    def update(
        self,
        epoch,
        total_epochs,
        loss,
        accuracy,
        val_loss=0.0,
        val_accuracy=0.0,
    ):

        with self.lock:

            self.epoch = int(epoch)
            self.total_epochs = int(total_epochs)

            self.loss = float(loss)
            self.accuracy = float(accuracy)

            self.val_loss = float(val_loss)
            self.val_accuracy = float(val_accuracy)

            self.progress = (
                int(epoch * 100 / total_epochs)
                if total_epochs > 0
                else 0
            )

            self.best_accuracy = max(
                self.best_accuracy,
                self.accuracy,
            )

            self.best_val_accuracy = max(
                self.best_val_accuracy,
                self.val_accuracy,
            )

            self.history.append(
                {
                    "epoch": self.epoch,
                    "loss": self.loss,
                    "accuracy": self.accuracy,
                    "val_loss": self.val_loss,
                    "val_accuracy": self.val_accuracy,
                    "progress": self.progress,
                    "timestamp": datetime.now().isoformat(),
                }
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

            "best_accuracy": self.best_accuracy,

            "best_val_accuracy": self.best_val_accuracy,

            "progress": self.progress,

            "training_time": self.training_time,

            "started_at": (
                self.started_at.isoformat()
                if self.started_at
                else None
            ),

            "finished_at": (
                self.finished_at.isoformat()
                if self.finished_at
                else None
            ),

            "logs": self.logs,

            "history": self.history,

            "error": self.error,
        }