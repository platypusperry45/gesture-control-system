from pydantic import BaseModel


class StatusResponse(BaseModel):
    camera: bool
    model_loaded: bool
    inference_running: bool
    prediction: str | None = None
    confidence: float
    action: str | None = None
    fps: float
    uptime: str