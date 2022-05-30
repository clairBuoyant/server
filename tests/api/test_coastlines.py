def test_coastlines(test_app):
    response = test_app.get("/api/v1/coastlines")
    assert response.status_code == 200

    rockaway_coastlines = response.json()
    assert len(rockaway_coastlines) == 11

    first_record = rockaway_coastlines[0]
    assert "buoy" in first_record
    assert "geom" in first_record
    assert "id" in first_record
    assert "station_id" in first_record
