from pybuoy import Buoy

from server.crud.crud_buoy import buoy
from server.schemas import BuoyCreate


async def seed_active_buoys(db):
    # OBS_ENDPOINT = "https://sdf.ndbc.noaa.gov/sos/server.php"

    def parse_activestations(stations):
        return [
            BuoyCreate(
                location=f"POINT({float(station.get('lon', 0.0))} {float(station.get('lat', 0.0))})",  # noqa: 501
                station_id=station.get("id"),
                name=station.get("name"),
                owner=station.get("owner"),
                elev=station.get("elev", 0.0),
                pgm=station.get("pgm"),
                type=station.get("type"),
                met=station.get("met", ""),
                currents=station.get("currents", ""),
                water_quality=station.get("waterquality", ""),
                dart=station.get("dart", ""),
                seq=station.get("seq", None),
            )
            for station in stations
        ]

    async def run():
        ndbc = Buoy()
        stations = ndbc.stations.get_active()

        parsed_stations = parse_activestations(stations=stations)
        return await buoy.create_many(db, parsed_stations)

    return await run()
