from pybuoy import Buoy

from server.crud.crud_buoy import buoy
from server.schemas import BuoyCreate


async def seed_active_buoys(db):
    # ACTIVESTATIONS_XML = "https://www.ndbc.noaa.gov/activestations.xml"
    # OBS_ENDPOINT = "https://sdf.ndbc.noaa.gov/sos/server.php"

    def parse_activestations(stations):
        return [
            BuoyCreate(
                location=f"POINT({float(station.get('lon', 0.0))} {float(station.get('lat', 0.0))})",
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

    async def persist_parsed(stations):
        # TODO: integrate pydantic layer with model layer
        return await buoy.create_buoys(db, stations)

    async def run():
        buoy = Buoy()
        stations = buoy.stations.get_active()

        parsed_stations = parse_activestations(stations=stations)

        return await persist_parsed(parsed_stations)

    return await run()
