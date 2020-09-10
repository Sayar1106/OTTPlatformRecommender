from fastapi import APIRouter, Depends
from starlette.requests import Request

from fastapi_skeleton.core import security
#todo create payload
from fastapi_skeleton.models.payload import HousePredictionPayload
from fastapi_skeleton.models.prediction import PlayListResult
# add model for request
from fastapi_skeleton.services.models import HousePriceModel

router = APIRouter()


@router.post("/playlist", response_model=PlayListResult, name="playlist")
def post_playlist(
    
    request: Request,
    authenticated: bool = Depends(security.validate_request),
    block_data: HousePredictionPayload = None
) -> PlayListResult:

    model: HousePriceModel = request.app.state.model
    prediction: HousePredictionResult = model.predict(block_data)

    return prediction
