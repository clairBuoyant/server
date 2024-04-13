from server.core.constants import BUOYS_URI

_rockaway_buoy_station_id = "44065"


def test_get_buoy(test_app):
    response = test_app.get(f"{BUOYS_URI}/{_rockaway_buoy_station_id}")
    assert response.status_code == 200

    rockaway_buoy = response.json()

    assert "id" in rockaway_buoy
    assert "station_id" in rockaway_buoy
    assert "name" in rockaway_buoy
    assert "owner" in rockaway_buoy
    assert "elev" in rockaway_buoy
    assert "pgm" in rockaway_buoy
    assert "type" in rockaway_buoy
    assert "met" in rockaway_buoy
    assert "currents" in rockaway_buoy
    assert "water_quality" in rockaway_buoy
    assert "dart" in rockaway_buoy
    assert "seq" in rockaway_buoy

    assert "location" in rockaway_buoy
    rockaway_buoy_location = rockaway_buoy["location"]
    assert len(rockaway_buoy_location) == 2
    assert rockaway_buoy["station_id"] == _rockaway_buoy_station_id


def test_get_buoys(test_app):
    response = test_app.get(BUOYS_URI)
    assert response.status_code == 200

    buoys = response.json()
    assert len(buoys) >= 1300

    assert "id" in buoys[0]
    assert "station_id" in buoys[0]
    assert "name" in buoys[0]
    assert "owner" in buoys[0]
    assert "location" in buoys[0]
    assert "elev" in buoys[0]
    assert "pgm" in buoys[0]
    assert "type" in buoys[0]
    assert "met" in buoys[0]
    assert "currents" in buoys[0]
    assert "water_quality" in buoys[0]
    assert "dart" in buoys[0]
    assert "seq" in buoys[0]
