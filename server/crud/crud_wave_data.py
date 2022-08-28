from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession  # type: ignore
from sqlalchemy.future import select  # type: ignore

from server.crud.base import CRUDBase
from server.models.wave_data import WaveData
from server.schemas.wave_data import WaveDataCreate, WaveDataUpdate


class CRUDWaveData(CRUDBase[WaveData, WaveDataCreate, WaveDataUpdate]):
    async def find_one(self, db: AsyncSession, date_recorded: datetime):
        result = await db.execute(
            select(WaveData).where(WaveData.date_recorded == date_recorded)
        )
        return result.scalars().first()

    async def find_all(self, db: AsyncSession):
        return await db.execute(select(WaveData))

    # TODO: Try to refactor this to follow DRY principle
    async def find_many_recordings(
        self,
        db: AsyncSession,
        station_id: str,
        begin_date: datetime,
        end_date: datetime,
    ):
        result = await db.execute(
            select(WaveData).where(
                WaveData.station_id == station_id
                and WaveData.date_recorded >= begin_date
                and WaveData.date_recorded <= end_date
            )
        )
        return result

    async def create_wave_data(self, db: AsyncSession, data: list[WaveDataCreate]):
        data_to_db = [
            WaveData(
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
        ]
        db.add_all(data_to_db)
        await db.commit()


wave_data = CRUDWaveData(WaveData)
