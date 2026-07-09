from tensorflow.keras.callbacks import Callback


class BackendTrainingCallback(Callback):

    def __init__(self, manager):
        super().__init__()
        self.manager = manager

    def on_train_begin(self, logs=None):

        self.manager.running = True
        self.manager.completed = False
        self.manager.stop_requested = False

        self.manager.add_log("Training started.")

    def on_epoch_end(self, epoch, logs=None):

        logs = logs or {}

        self.manager.update(

            epoch=epoch + 1,

            total_epochs=self.params.get("epochs", 0),

            loss=float(logs.get("loss", 0)),

            accuracy=float(logs.get("accuracy", 0)),

            val_loss=float(logs.get("val_loss", 0)),

            val_accuracy=float(logs.get("val_accuracy", 0)),
        )

        self.manager.add_log(
            f"Epoch {epoch+1}/{self.params.get('epochs',0)} | "
            f"Loss {logs.get('loss',0):.4f} | "
            f"Accuracy {logs.get('accuracy',0):.4f}"
        )

        if self.manager.stop_requested:
            self.model.stop_training = True

    def on_train_end(self, logs=None):

        self.manager.running = False

        if self.manager.stop_requested:

            self.manager.add_log("Training stopped.")

        else:

            self.manager.completed = True

            self.manager.add_log("Training completed successfully.")