import pytest
from unittest.mock import MagicMock
from project import get_weather, get_forecast, return_weather_forecast, WeatherError
from datetime import date, timedelta

def test_get_weather_request(mocker):
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "cod": 200,
        "name": "city",
        "sys": {"country": "country"},
        "main": {
            "temp": 33.0,
            "feels_like": 30.0,
            "humidity": 50
        },
        "weather": [{"description": "clear sky"}]
    }
    mocker.patch('requests.get', return_value=mock_response)

    assert get_weather("api_key", "city", "unit") == {
        "city": "city",
        "country": "country",
        "temp": 33.0,
        "feels_like": 30.0,
        "desc": "clear sky",
        "humidity": 50
    }

def test_get_weather_error(mocker):
    mock_response = MagicMock()
    mock_response.json.return_value = {"cod": "404", "message": "City not found"}
    mocker.patch('requests.get', return_value=mock_response)

    with pytest.raises(WeatherError):
        get_weather("api_key", "wrong_city_name", "unit")

    mock_response.json.return_value = {"cod": "401", "message": "Unauthorized"}
    mocker.patch('requests.get', return_value=mock_response)

    with pytest.raises(WeatherError):
        get_weather("wrong_api_key", "city_name", "unit")

def test_get_forecast_request(mocker):
    tomorrow = date.today() + timedelta(days=1)
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "cod": "200",
        "list": [
            {"dt_txt": f"{tomorrow} 00:00:00", "main": {"temp": 33.0}, "rain": {"3h": 0.3}},
            {"dt_txt": f"{tomorrow} 03:00:00", "main": {"temp": 30.0}, "rain": {"3h": 2.0}},
            {"dt_txt": f"{tomorrow} 06:00:00", "main": {"temp": 25.0}, "rain": {"3h": 5.0}},
        ]
    }
    mocker.patch('requests.get', return_value=mock_response)

    assert get_forecast("api_key", "city", "unit") == {
        "date": tomorrow.isoformat(),
        "temp_max": 33.0,
        "temp_min": 25.0,
        "rain_prob": 7.3
    }

def test_get_forecast_error(mocker):
    mock_response = MagicMock()
    mock_response.json.return_value = {"cod": "404", "message": "City not found"}
    mocker.patch('requests.get', return_value=mock_response)

    with pytest.raises(WeatherError):
        get_forecast("api_key", "wrong_city_name", "unit")

    mock_response.json.return_value = {"cod": "401", "message": "Unauthorized"}
    mocker.patch('requests.get', return_value=mock_response)

    with pytest.raises(WeatherError):
        get_forecast("wrong_api_key", "city_name", "unit")

def test_return_weather_forecast():
    weather_info = {
        "city": "City",
        "country": "CT",
        "temp": 33.0,
        "feels_like": 30.0,
        "desc": "clear sky",
        "humidity": 50
    }
    forecast_info = {
        "date": "2024-08-27",
        "temp_max": 33.0,
        "temp_min": 25.0,
        "rain_prob": 7.3
    }
    unit = "metric"
    assert return_weather_forecast(weather_info, forecast_info, unit) == (
        "\n---Current Weather---"
        "\nCity: City, CT"
        "\nDescription: Clear sky"
        "\nTemperature: 33.0°C feels like 30.0°C"
        "\nHumidity: 50%"
        "\n\n---Tomorrow Forecast---"
        "\nMax Temperature: 33.0°C"
        "\nMin Temperature: 25.0°C"
        "\nRain Probability: 7.30%"
        "\n"
    )
