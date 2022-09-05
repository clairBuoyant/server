from server.core.constants import WAVE_DATA_URI


def test_get_wave_data(test_app):
    response = test_app.get(WAVE_DATA_URI)
    assert response.status_code == 200

    wave_data = response.json()

    first_record = wave_data[0]
    assert "id" in first_record
    assert "station_id" in first_record
    assert "date_recorded" in first_record
    assert "significant_wave_height" in first_record
    assert "swell_height" in first_record
    assert "swell_period" in first_record
    assert "wind_wave_height" in first_record
    assert "wind_wave_period" in first_record
    assert "swell_direction" in first_record
    assert "wind_wave_direction" in first_record
    assert "steepness" in first_record
    assert "average_wave_period" in first_record
    assert "mean_wave_direction" in first_record

    # TODO: Create JOIN test
