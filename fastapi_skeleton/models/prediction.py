

from pydantic import BaseModel
from fastapi_skeleton.models.payload import (song)

class HousePredictionResult(BaseModel):
    median_house_value: int
    currency: str = "USD"
