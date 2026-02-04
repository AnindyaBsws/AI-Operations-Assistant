import requests

class WeatherTool:
    def get_weather(self, city: str):
        # Simple city → lat/long mapping (minimal, acceptable)
        city_coords = {
            "Berlin": (52.52, 13.41),
            "London": (51.51, -0.13),
            "New York": (40.71, -74.01)
        }

        if city not in city_coords:
            return {"error": "City not supported"}

        lat, lon = city_coords[city]
        url = (
            f"https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current_weather=true"
        )

        res = requests.get(url, timeout=10)
        res.raise_for_status()
        return res.json()
