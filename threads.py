import asyncio

from app_state import AppState
from apps.display import display_loop
from apps.weather import weather_loop


def run_display_loop(a: AppState):
    return asyncio.run(display_loop(a))


def run_weather_loop(a: AppState):
    return asyncio.run(weather_loop(a))


threads = {
    "weather": run_weather_loop,
    "display": run_display_loop,
}
