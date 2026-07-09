from pydantic import BaseModel


class Gesture(BaseModel):
    name: str