from server.api.api_router import APIRouter
from server.api.dependencies import CurrentAsyncDBSession
from server.core.constants import RELATIVE_ROOT
from server.crud import forecast
from server.schemas import Forecast

router = APIRouter()


@router.get(RELATIVE_ROOT, response_model=list[Forecast])
async def get_forecasts(db_session: CurrentAsyncDBSession):
    return await forecast.find_many(db_session=db_session)


# TODO: write out remaining query endpoints
