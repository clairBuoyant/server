import requests

from bs4 import BeautifulSoup as bs

from db.crud import create_buoys
from db.schemas import BuoyCreate


async def NDBCScraper_Buoy(db):
    """NDBC Scraper.
    Request Parameters for Observations.
        request = GetObservation
        service = SOS
        version = 1.0.0
        offering = urn:ioos:station:wmo::<station ID> for single station,
            or urn:ioos:network:noaa.nws.ndbc:all for use with collections.
        observedproperty = one of the following:
            air_pressure_at_sea_level
            air_temperature
            currents
            sea_floor_depth_below_sea_surface (water level for tsunami stations)
            sea_water_electrical_conductivity
            sea_water_salinity
            sea_water_temperature
            waves
        responseformat=text/csv
    """
    ACTIVESTATIONS_XML = "https://www.ndbc.noaa.gov/activestations.xml"
    # OBS_ENDPOINT = "https://sdf.ndbc.noaa.gov/sos/server.php"

    def get_activestations():
        """Extract NDBC's activestations from `activestations.xml` endpoint."""
        xml_data = requests.get(ACTIVESTATIONS_XML).content

        soup = bs(xml_data, "xml")
        return soup.find_all("station")

    def parse_activestations(stations):
        parsed_stations_obj = []
        for station in stations:
            station = station.attrs
            lon, lat = float(station.get("lon", 0.0)), float(station.get("lat", 0.0))
            geo = f"Point({lon} {lat})"

            parsed_stations_obj.append(
                BuoyCreate(
                    location=geo,
                    station_id=station.get("id"),
                    name=station.get("name"),
                    owner=station.get("owner"),
                    elev=station.get("elev", 0.0),
                    pgm=station.get("pgm"),
                    buoy_type=station.get("type"),
                    met=station.get("met", ""),
                    currents=station.get("currents", ""),
                    waterquality=station.get("waterquality", ""),
                    dart=station.get("dart", ""),
                    seq=station.get("seq", None),
                )
            )
        return parsed_stations_obj

    async def persist_parsed(stations):
        # TODO: integrate pydantic layer with model layer
        return await create_buoys(db, stations)

    async def seed_buoy_data():
        stations = parse_activestations(get_activestations())
        return await persist_parsed(stations)

    return await seed_buoy_data()


if __name__ == "__main__":
    NDBCScraper_Buoy()
