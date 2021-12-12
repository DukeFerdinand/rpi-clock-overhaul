from multiprocessing import Process
from queue import Queue
import asyncio
from time import sleep

from gpiozero import LED
from typing import List
from dotenv import load_dotenv

import I2C_LCD_driver
from threads import threads
from app_state import AppState

# LCD I2C Address
# Get this by calling `sudo i2cdetect -y 1` in your terminal

ADDRESS = 0x27

# Globals
led: LED
lcd = I2C_LCD_driver.lcd(ADDRESS)
queue = Queue()

loop_active: bool = True
message_shown: bool = False

app: AppState


async def setup():
    global led
    global app

    # Pick up env vars
    load_dotenv()

    app = AppState()
    await app.get_weather()

    led = LED(26)


def blinker_event_loop(_a: AppState):
    while loop_active:
        print("Loop!")
        if led is not None:
            led.on()
            sleep(1)
            led.off()
            sleep(1)


def display_loop(a: AppState):
    async def run_display_loop():
        global message_shown
        while loop_active:
            weather_string = a.weather()['weather'][0]['description']
            if not message_shown:
                print("Setting lcd")
                lcd.lcd_clear()
                lcd.lcd_display_string("Hello, Pi Controller", 1)
                lcd.lcd_display_string("Current weather ->", 2)
                lcd.lcd_display_string(f"  {weather_string}", 3)
                message_shown = True

            sleep(10)

    return asyncio.run(run_display_loop())


processes: List[Process] = []


async def main():
    global processes
    await setup()
    for thread in threads.keys():
        print(f"Starting thread: {thread}")
        p = Process(target=threads[thread], args=(app,))
        p.start()
        processes.append(p)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Received interrupt, stopping process...")
        for proc in processes:
            proc.terminate()
