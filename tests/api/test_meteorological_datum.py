from server.core.constants import METEOROLOGICAL_DATA_URI

def test_get_meteorological_data(test_app):
    response = test_app.get(METEOROLOGICAL_DATA_URI)
    assert response.status_code == 200

    meteorological_data = response.json()

    first_record = meteorological_data[0]
    assert "id" in first_record
    assert "station_id" in first_record
    assert "date_recorded" in first_record
    assert "wind_direction" in first_record
    assert "wind_speed" in first_record
    assert "wind_gust" in first_record
    assert "wind_height" in first_record
    assert "dominant_wave_period" in first_record
    assert "average_wave_period" in first_record
    assert "wave_direction" in first_record
    assert "sea_level_pressure" in first_record
    assert "pressure_tendency" in first_record
    assert "air_temperature" in first_record
    assert "water_temperature" in first_record
    assert "dewpoint_temperature" in first_record
    assert "visibility" in first_record
    assert "tide" in first_record