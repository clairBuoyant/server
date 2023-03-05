from datetime import datetime, timedelta

from pybuoy import Buoy
from sqlalchemy.ext.asyncio import AsyncSession

from server.crud import buoy, coastline, forecast, meteorological_datum, wave_datum
from server.schemas import (
    BuoyCreate,
    CoastlineCreate,
    ForecastCreate,
    MeteorologicalDatumCreate,
    WaveDatumCreate,
)

NDBC = NOAA = Buoy()
ROCKAWAY_STATION_ID = "44065"
ROCKAWAY_STATION_LOC = {"lat": 40.369, "lon": -73.703}


async def seed_active_buoys(db_session: AsyncSession):
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
        stations = NDBC.stations.get_active()

        parsed_stations = parse_activestations(stations=stations)
        return await buoy.create_many(db_session, parsed_stations)

    return await run()


# flake8: noqa
# ! TMP - hardcoded for MVP
rockaway_coastlines: list[tuple] = [
    (
        "44065",
        "MULTILINESTRING((-73.75454880635496 40.59037602897099,-73.7545695 40.5903755,-73.7556942 40.5904583,-73.7589375 40.5909509,-73.7606906 40.5911573,-73.7622596 40.5912771,-73.7639689 40.5914035,-73.7648542 40.5914169,-73.765985 40.5913703,-73.7674664 40.5911639,-73.7679572 40.5910308,-73.7681413 40.5910641,-73.7687198 40.5911639,-73.7697892 40.591104,-73.770771 40.5909176,-73.7711128 40.5909243,-73.7722699 40.5908178,-73.77289246641112 40.590727323271096))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.77289246641112 40.590727323271096,-73.7765299 40.5901987,-73.7771085 40.5901987,-73.7888328 40.587908,-73.79107085068254 40.587470759210284))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.79107085068254 40.587470759210284,-73.7912933 40.5874273,-73.7937135 40.5869544,-73.7961655 40.5864753,-73.7986058 40.5859985,-73.801107 40.5855098,-73.8035011 40.585042,-73.8058255 40.5845879,-73.8082891 40.5839493,-73.80917154614897 40.583762885019496))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.80917154614897 40.583762885019496,-73.8106593 40.5834486,-73.8113481 40.5836178,-73.8130288 40.5832455,-73.8156063 40.5823766,-73.8178899 40.5815672,-73.8209719 40.5807761,-73.8230454 40.5801759,-73.8253852 40.5794711,-73.82693126749244 40.579050380227095))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.82693126749244 40.579050380227095,-73.8282714 40.5786857,-73.8302824 40.5780627,-73.8326628 40.5774004,-73.8349023 40.5766669,-73.8364042 40.5761432,-73.8384384 40.575451,-73.8411682 40.574588,-73.8439354 40.5736275,-73.8445312970996 40.573430558306164))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.8445312970996 40.573430558306164,-73.84531 40.5731732,-73.847357 40.5726834,-73.8496859 40.5719095,-73.8527806 40.5706851,-73.8536344 40.5703354,-73.8567626 40.5692976,-73.857957 40.5688481,-73.8592028 40.568381,-73.860114 40.5680387,-73.8609553 40.5676538,-73.8619414743923 40.567294052172684))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.8619414743923 40.567294052172684,-73.8623328 40.5671513,-73.8629851 40.566684,-73.8635322 40.566924,-73.864375 40.5667296,-73.8649727 40.5666036,-73.8666434 40.5661502,-73.8685761 40.5656257,-73.8706933 40.5649302,-73.8725745 40.5641611,-73.8727054 40.564132,-73.8729249 40.5641479,-73.8756746 40.563292,-73.8777069 40.5625415,-73.87940606826581 40.56196782402439))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.87940606826581 40.56196782402439,-73.8795258 40.5619274,-73.8795643 40.5619144,-73.8896822 40.5590204,-73.8921778 40.5582555,-73.8926346 40.5581886,-73.8949549 40.5574476,-73.8952913 40.5575724,-73.8971065 40.5570183,-73.89713175380928 40.55702269449192))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.89713175380928 40.55702269449192,-73.8976283 40.5571091,-73.9006268 40.5566578,-73.9015865 40.5566633,-73.9026604 40.5563436,-73.9037119 40.5560501,-73.9053185 40.5554833,-73.9088425 40.5543162,-73.9094305 40.5540534,-73.9147849266448 40.55206278385212))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.9147849266448 40.55206278385212,-73.9246945 40.5483787,-73.926394 40.5476649,-73.930222 40.5460766,-73.93202559976382 40.54541645922031))",
    ),
    (
        "44065",
        "MULTILINESTRING((-73.93202559976382 40.54541645922031,-73.9340205 40.5446863,-73.9365282 40.5437426,-73.9384916 40.5427764,-73.9394879 40.54232,-73.9406072943117 40.54191192909479))",
    ),
]


# Rockaway coastline
async def seed_coastlines(db_session: AsyncSession):
    parsed_coastlines = [
        CoastlineCreate(geom=geom_coastline, station_id=station_id)
        for station_id, geom_coastline in rockaway_coastlines
    ]
    return await coastline.create_many(db_session, parsed_coastlines)


async def seed_forecast_data(
    db_session: AsyncSession, station_location: dict[str, float] = ROCKAWAY_STATION_LOC
):
    arbitrary_start = (datetime.now() + timedelta(1)).isoformat()
    arbitrary_end = (datetime.now() + timedelta(5)).isoformat()

    data = NDBC.forecasts.get(
        lat=station_location["lat"],
        lon=station_location["lon"],
        start_date=arbitrary_start,
        end_date=arbitrary_end,
    )
    # TODO: remove object from memory
    parsed_meteorological_data = [
        # TODO: pybuoy – investigate better design
        # `value` needed due to custom float type
        # to use `None` instead of `NaN`.
        ForecastCreate(
            # TODO: pybuoy – need for `replace` a bug
            date_recorded=datum.datetime.replace(tzinfo=None),
            # TODO: link lon&lat to station_id dynamically
            station_id=ROCKAWAY_STATION_ID,
            wave_height=datum.wave_height.value,
            wind_direction=datum.wind_direction.value,
            wind_speed=datum.wind_speed.value,
            wind_speed_gust=datum.wind_gust.value,
        )
        for datum in data
    ]
    return await forecast.create_many(db_session, parsed_meteorological_data)


async def seed_meteorological_data(
    db_session: AsyncSession, station_id: str = ROCKAWAY_STATION_ID
):
    data = NDBC.realtime.get(station_id=station_id)
    # TODO: remove object from memory
    parsed_meteorological_data = [
        MeteorologicalDatumCreate(
            station_id=station_id,
            date_recorded=datum.datetime,
            wind_direction=datum.wind_direction.value,
            wind_speed=datum.wind_speed.value,
            wind_gust=datum.wind_gust.value,
            wave_height=datum.wave_height.value,
            dominant_wave_period=datum.dominant_wave_period.value,
            average_wave_period=datum.average_wave_period.value,
            wave_direction=datum.wave_direction.value,
            sea_level_pressure=datum.sea_level_pressure.value,
            pressure_tendency=datum.pressure_tendency.value,
            air_temperature=datum.air_temperature.value,
            water_temperature=datum.water_temperature.value,
            dewpoint_temperature=datum.dewpoint_temperature.value,
            visibility=datum.visibility.value,
            tide=datum.tide.value,
        )
        for datum in data
    ]
    return await meteorological_datum.create_many(
        db_session, parsed_meteorological_data
    )


async def seed_wave_data(
    db_session: AsyncSession, station_id: str = ROCKAWAY_STATION_ID
):
    data = NDBC.realtime.get(station_id=station_id, dataset="spec")
    parsed_wave_data = [
        WaveDatumCreate(
            station_id=station_id,
            date_recorded=datum.datetime,
            significant_wave_height=datum.significant_wave_height.value,
            swell_height=datum.swell_height.value,
            swell_period=datum.swell_period.value,
            wind_wave_height=datum.wind_wave_height.value,
            wind_wave_period=datum.wind_wave_period.value,
            swell_direction=datum.swell_direction.value,
            wind_wave_direction=datum.wind_wave_direction.value,
            steepness=datum.steepness.value,
            average_wave_period=datum.average_wave_period.value,
            mean_wave_direction=datum.dominant_wave_direction.value,
        )
        for datum in data
    ]
    return await wave_datum.create_many(db_session, parsed_wave_data)
