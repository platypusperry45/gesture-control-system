from pydantic import BaseModel


class Prediction(BaseModel):
    prediction: str | None = None
    confidence: float = 0.0