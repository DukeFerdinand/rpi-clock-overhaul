from asyncio import sleep

import I2C_LCD_driver
from app_state import AppState

ADDRESS = 0x27


async def display_loop(a: AppState):
    lcd = I2C_LCD_driver.lcd(ADDRESS)
    while True:
        weather_string = a.weather()
        # if not a.message_shown:
        print("Setting lcd")
        lcd.lcd_clear()
        lcd.lcd_display_string("Current weather ->", 1)
        lcd.lcd_display_string(f"  {weather_string}", 2)
        a.set_message_shown(True)

        await sleep(10)
