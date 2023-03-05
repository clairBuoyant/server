from server.api.api_router import APIRouter
from server.api.dependencies import CurrentAsyncDBSession
from server.core.constants import RELATIVE_ROOT
from server.crud import meteorological_datum
from server.schemas import MeteorologicalDatum

router = APIRouter()


@router.get(RELATIVE_ROOT, response_model=list[MeteorologicalDatum])
async def get_meteorological_data(db_session: CurrentAsyncDBSession):
    return await meteorological_datum.find_many(db_session=db_session)


# TODO: write out remaining query endpoints
