from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore

from server.crud.base import CRUDBase
from server.models.wave_datum import WaveDatum
from server.schemas.wave_datum import WaveDatumCreate, WaveDatumUpdate


class CRUDWaveDatum(CRUDBase[WaveDatum, WaveDatumCreate, WaveDatumUpdate]):
    async def create_many(self, db_session: AsyncSession, data: list[WaveDatumCreate]):
        return await super().create_many(
            db_session,
            [
                WaveDatum(
                    station_id=datum.station_id,
                    date_recorded=datum.date_recorded,
                    significant_wave_height=datum.significant_wave_height,
                    swell_height=datum.swell_height,
                    swell_period=datum.swell_period,
                    wind_wave_height=datum.wind_wave_height,
                    wind_wave_period=datum.wind_wave_period,
                    swell_direction=datum.swell_direction,
                    wind_wave_direction=datum.wind_wave_direction,
                    steepness=datum.steepness,
                    average_wave_period=datum.average_wave_period,
                    mean_wave_direction=datum.mean_wave_direction,
                )
                for datum in data
            ],
        )


wave_datum = CRUDWaveDatum(WaveDatum)
