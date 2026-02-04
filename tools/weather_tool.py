import requests
import os

class WeatherTool:
    def get_weather(self, city: str):
        api_key = os.getenv("WEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        return requests.get(url).json()
