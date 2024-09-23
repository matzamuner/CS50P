# Weather Forecast App
#### Video Demo:  https://www.youtube.com/watch?v=1IEswtjWbxo
#### Description:

This Python project provides a command-line tool that fetches and displays the current weather information and a one-day forecast for a given city, allowing users to choose the temperature unit for display. It uses the OpenWeather API to retrieve detailed weather data, including the current temperature, feels-like temperature, weather description, and humidity. Additionally, it forecasts the maximum and minimum temperatures and the probability of rain for the following day.

## Features

- Fetch current weather for a given city.
- Fetch a forecast for the next day.
- Display the weather data in metric (°C), imperial (°F) or the default Kelvin (K) units.
- Handle errors such as invalid requests, unauthorized access or city not found.

## Project Structure

- **`project.py`**: Contains the core application script for fetching and displaying weather data.
- **`test_project.py`**: Contains unit tests for the core functionality using `pytest` and `pytest-mock`.

## Files

### `project.py`

This file contains the main functionality of the weather forecasting tool:

- **`WeatherError`**: A custom exception class for handling weather-related errors.
- **`main()`**: Prompts the user for a city and desired unit, fetches the weather and forecast data, and prints the results.
- **`get_weather(api_key: str, city: str, unit: str) -> dict`**: Fetches the current weather for a city.
- **`get_forecast(api_key: str, city: str, unit: str) -> dict`**: Fetches for the weather forecast of the given city for the following day.
- **`return_weather_forecast(weather_info: dict, forecast_info: dict, unit: str) -> str`**: Formats the weather and forecast data into a readable string.

### `test_project.py`

This file contains unit tests for the functionality in `project.py`:

- **`test_get_weather_request(mocker)`**: Tests successful retrieval of weather data.
- **`test_get_weather_error(mocker)`**: Tests handling of errors when fetching weather data.
- **`test_get_forecast_request(mocker)`**: Tests successful retrieval of forecast data.
- **`test_get_forecast_error(mocker)`**: Tests handling of errors when fetching forecast data.
- **`test_return_weather_forecast()`**: Tests the formatting of the weather and forecast.

## Requirements

To run this project, you need Python installed on your machine. You also need to install the required Python packages on `requirements.txt`, you can do so by running:

```bash
pip install -r requirements.txt
```

## Usage

1. **Add your OpenWeatherMap API key**:

   Replace `"your_api_key"` in the `project.py` script with your own API key from OpenWeatherMap.

2. **Run the application**:

    ```bash
    python project.py
    ```

   Follow the prompts to enter a city name and a unit for display. The application will display the current weather and the forecast for tomorrow.

## Testing

To run the tests, ensure you have `pytest` and `pytest-mock` installed.

Use `pytest`:

```bash
pytest test_project.py
```
