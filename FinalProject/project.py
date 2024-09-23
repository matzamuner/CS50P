import requests
from datetime import date, timedelta

class WeatherError(Exception):
    """
    Exception for weather errors
    """
    pass

def main():
    API_KEY = "your_api_key"
    city = input("City: ").strip()
    unit = input("Temperature Unit(metric/imperial/standard): ").lower().strip()
    weather_info = get_weather(API_KEY, city, unit)
    forecast_info = get_forecast(API_KEY, city, unit)
    print(return_weather_forecast(weather_info, forecast_info, unit))

def get_weather(api_key: str, city: str, unit: str) -> dict:
    """
    Fetches current weather in a given city
    """
    try:
        payload = {
            "q": city,
            "appid": api_key,
            "units": unit
            }
        r = requests.get("https://api.openweathermap.org/data/2.5/weather", params=payload)
    except requests.RequestException:
        raise WeatherError("Invalid request")
    data = r.json()
    if data["cod"] != 200:
        error_message = data["message"]
        if data["cod"] == "404":
            raise WeatherError("City not found")
        elif data["cod"] == 401:
            raise WeatherError("Unauthorized. Check API key")
        else:
            raise WeatherError(error_message)
    return {
            "city": data["name"],
            "country": data["sys"]["country"],
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "desc": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
        }

def get_forecast(api_key: str, city: str, unit: str) -> dict:
    """
    Fetches weather forecast in a given city
    """
    try:
        payload = {
            "q": city,
            "appid": api_key,
            "units": unit
        }
        r = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=payload)
    except requests.RequestException:
        raise WeatherError("Invalid request")
    data = r.json()
    if data["cod"] != "200":
        error_message = data["message"]
        if data["cod"] == "404":
            raise WeatherError("City not found")
        elif data["cod"] == 401:
            raise WeatherError("Unauthorized. Check API key")
        else:
            raise WeatherError(error_message)
    else:
        tomorrow = date.today() + timedelta(days=1)
        temp_max = float("-inf")
        temp_min = float("inf")
        rain_prob = 0.0
        for node in data["list"]:
            if str(tomorrow) in node["dt_txt"]:
                temp = node["main"]["temp"]
                temp_max = max(temp_max, temp)
                temp_min = min(temp_min, temp)
                if "rain" in node:
                    rain_prob += node["rain"]["3h"]
        rain_prob = min(rain_prob, 100.0)
        return {
            "date": tomorrow.isoformat(),
            "temp_max": temp_max,
            "temp_min": temp_min,
            "rain_prob": rain_prob
        }

def return_weather_forecast(weather_info: dict, forecast_info: dict, unit: str) -> str:
    """
    Returns formated weather forecast
    """
    match unit:
        case "metric":
            unit_label = "°C"
        case "imperial":
            unit_label = "°F"
        case _:
            unit_label = "K"
    return ("\n---Current Weather---"
    f"\nCity: {weather_info["city"]}, {weather_info["country"]}"
    f"\nDescription: {weather_info["desc"].capitalize()}"
    f"\nTemperature: {weather_info["temp"]}{unit_label} feels like {weather_info["feels_like"]}{unit_label}"
    f"\nHumidity: {weather_info["humidity"]}%\n"
    "\n---Tomorrow Forecast---"
    f"\nMax Temperature: {forecast_info["temp_max"]}{unit_label}"
    f"\nMin Temperature: {forecast_info["temp_min"]}{unit_label}"
    f"\nRain Probability: {forecast_info["rain_prob"]:.2f}%\n")

if __name__ == "__main__":
    main()
