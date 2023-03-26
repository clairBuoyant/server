from server.core.constants import FORECASTS_URI


def test_get_forecasts(test_app):
    response = test_app.get(FORECASTS_URI)
    assert response.status_code == 200

    forecast_data = response.json()

    first_record = forecast_data[0]
    assert "id" in first_record
    assert "station_id" in first_record
    assert "date_recorded" in first_record
    assert "wave_height" in first_record
    assert "wind_direction" in first_record
    assert "wind_speed" in first_record
    assert "wind_speed_gust" in first_record

    # TODO: Create JOIN test
