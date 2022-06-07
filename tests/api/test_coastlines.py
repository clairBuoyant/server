from server.core.constants import COASTLINES_URI


def test_coastlines(test_app):
    response = test_app.get(COASTLINES_URI)
    assert response.status_code == 200

    rockaway_coastlines = response.json()
    assert len(rockaway_coastlines) == 11

    first_record = rockaway_coastlines[0]
    assert "buoy" in first_record
    assert "geom" in first_record
    assert "id" in first_record
    assert "station_id" in first_record
