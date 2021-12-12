from asyncio import sleep

from app_state import AppState


async def weather_loop(a: AppState):
    while True:
        await a.get_weather()

        await sleep(10)
