from requests import get


class WeatherService:
    API_KEY: str
    weather: dict

    def __init__(self, key: str):
        self.API_KEY = key

    async def get_weather(self):
        url = f'https://api.openweathermap.org/data/2.5/weather?q=Philadelphia&appid={self.API_KEY}'
        self.weather = get(url).json()
        return self.weather

    def get_weather_description(self):
        return self.weather['weather'][0]['description'] or 'N/A'
