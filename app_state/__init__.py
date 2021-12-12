import os
from typing import NewType
from queue import Queue

from gpiozero import LED

from .services import weather

State = NewType('State', dict)


class AppState:
    weather_service: weather.WeatherService
    state: State
    message_shown: bool = False
    led: LED

    def __init__(self):
        weather_key = os.environ.get('WEATHER_API_KEY')
        self.weather_service = weather.WeatherService(weather_key)

    def set_message_shown(self, b: bool):
        self.message_shown = b

    def weather(self):
        return self.weather_service.get_weather_description()

    async def get_weather(self):
        print("Updating weather")
        await self.weather_service.get_weather()
        print("Got new weather data")
