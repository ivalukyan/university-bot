import pytz

from datetime import datetime
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, WebAppInfo, CallbackQuery
)


async def check_telegram_ids(user_id: int) -> bool:

    telegram_ids = [877008114]

    if user_id in telegram_ids:
        return True
    return False


async def time_for_dialog() -> str:

    tz_Moscow = pytz.timezone('Europe/Moscow')
    hour = datetime.now(tz=tz_Moscow).hour

    if hour in [18, 19, 20, 21, 22, 23, 0, 1, 2]:
        return "Добрый вечер"
    elif hour in [3, 4, 5, 6, 7, 8, 9, 10, 11]:
        return "Доброе утро"
    else:
        return "Добрый день"
    

async def create_calandar(month: int) -> list:

    tz_Moscow = pytz.timezone('Europe/Moscow')
    m = datetime.now(tz=tz_Moscow).month
    y = datetime.now(tz=tz_Moscow).year

    mon = []
    week = []
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8:31, 9: 30, 10: 31, 11: 30, 12: 31}

    day = 1

    while day != months[month]:

        for _ in range(6):

            week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}-{m}-{y}"))

            day += 1

            if day == months[month]:
                week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}-{m}-{y}"))
                break

        mon.append(week)
        week = []

    mon.append([InlineKeyboardButton(text="Назад", callback_data="back")])

    return mon
