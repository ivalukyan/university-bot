import pytz
import pandas as pd

from datetime import datetime
from database.db import Session, User
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, WebAppInfo, CallbackQuery
)


async def check_telegram_ids(user_id: int) -> bool:

    db_session = Session()
    ids = db_session.query(User.telegram_id).all()
    telegram_ids = [_[0] for _ in ids]

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

            week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"))

            day += 1

            if day == months[month]:
                week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"))
                break

        mon.append(week)
        week = []

    mon.append([InlineKeyboardButton(text="Назад", callback_data="back")])

    return mon


async def insert_info_abt_users(fullname: str, telegram_id: int):
    excel_data = pd.read_excel("files/users.xlsx")

    ids = [_[1] for _ in excel_data.values.tolist()]

    if not telegram_id in ids:
        to_append_xlsx = pd.DataFrame({
            'Имя пользователя': [fullname],
            'ID пользователя': [telegram_id]
        })

        df = excel_data._append(to_append_xlsx, ignore_index=True)
        
        df.to_excel("files/users.xlsx", index=False)
