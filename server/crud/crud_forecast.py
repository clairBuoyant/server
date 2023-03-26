from sqlalchemy.ext.asyncio import AsyncSession

from server.crud.base import CRUDBase
from server.models.forecast import Forecast
from server.schemas.forecast import ForecastCreate, ForecastUpdate


class CRUDForecast(CRUDBase[Forecast, ForecastCreate, ForecastUpdate]):
    async def create_many(self, db_session: AsyncSession, data: list[ForecastCreate]):
        return await super().create_many(
            db_session,
            [
                Forecast(
                    date_recorded=datum.date_recorded,
                    station_id=datum.station_id,
                    wave_height=datum.wave_height,
                    wind_direction=datum.wind_direction,
                    wind_speed=datum.wind_speed,
                    wind_speed_gust=datum.wind_speed_gust,
                )
                for datum in data
            ],
        )


forecast = CRUDForecast(Forecast)
