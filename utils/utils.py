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
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    mon.append([
        InlineKeyboardButton(text='Пн', callback_data='Mon'),
        InlineKeyboardButton(text='Вт', callback_data='Tue'),
        InlineKeyboardButton(text='Ср', callback_data='Wed'),
        InlineKeyboardButton(text='Чт', callback_data='Thu'),
        InlineKeyboardButton(text='Пт', callback_data='Fri'),
        InlineKeyboardButton(text='Сб', callback_data='Sat'),
        InlineKeyboardButton(text='Вс', callback_data='Sun')
    ])

    print(datetime(y, m, 1).strftime('%a'))

    res = await wk(mon=mon, first_day=datetime(y, m, 1).strftime('%a'))

    day = res[1]

    mon = res[0]

    while day != months[month]:

        for _ in range(7):

            week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"))

            day += 1

            if day == months[month]:

                if _ == 6:
                    mon.append(week)
                    mon.append([InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"),
                                InlineKeyboardButton(text="1", callback_data="data"),
                                InlineKeyboardButton(text="2", callback_data="data"),
                                InlineKeyboardButton(text="3", callback_data="data"),
                                InlineKeyboardButton(text="4", callback_data="data"),
                                InlineKeyboardButton(text="5", callback_data="data"),
                                InlineKeyboardButton(text="6", callback_data="data")])
                    week = []
                    break
                elif _ == 5:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"))
                    week.append(InlineKeyboardButton(text="1", callback_data="data"))
                    week.append(InlineKeyboardButton(text="2", callback_data="data"))
                    week.append(InlineKeyboardButton(text="3", callback_data="data"))
                    week.append(InlineKeyboardButton(text="4", callback_data="data"))
                    week.append(InlineKeyboardButton(text="5", callback_data="data"))
                    break

                elif _ == 4:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"))
                    week.append(InlineKeyboardButton(text="1", callback_data="data"))
                    week.append(InlineKeyboardButton(text="2", callback_data="data"))
                    week.append(InlineKeyboardButton(text="3", callback_data="data"))
                    week.append(InlineKeyboardButton(text="4", callback_data="data"))
                    break

                elif _ == 3:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"))
                    week.append(InlineKeyboardButton(text="1", callback_data="data"))
                    week.append(InlineKeyboardButton(text="2", callback_data="data"))
                    week.append(InlineKeyboardButton(text="3", callback_data="data"))
                    break

                elif _ == 2:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"))
                    week.append(InlineKeyboardButton(text="1", callback_data="data"))
                    week.append(InlineKeyboardButton(text="2", callback_data="data"))
                    break

                elif _ == 1:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"))
                    week.append(InlineKeyboardButton(text="1", callback_data="data"))
                    break

                else:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}"))
                    break

        mon.append(week)
        week = []

    mon.append([InlineKeyboardButton(text="⬅️", callback_data=f"before_tasks"),
                InlineKeyboardButton(text="➡️", callback_data=f"after_tasks")])
    mon.append([InlineKeyboardButton(text="Назад", callback_data="back")])

    return mon


async def insert_info_abt_users(fullname: str, telegram_id: int, username: str):
    excel_data = pd.read_excel("files/users.xlsx")

    ids = [_[1] for _ in excel_data.values.tolist()]

    if not telegram_id in ids:
        to_append_xlsx = pd.DataFrame({
            'Имя пользователя': [fullname],
            'ID пользователя': [telegram_id],
            'Ник пользователя': [username]
        })

        df = excel_data._append(to_append_xlsx, ignore_index=True)

        df.to_excel("files/users.xlsx", index=False)


async def fullname(message) -> str:
    db_session = Session()
    result = db_session.query(User).filter(User.telegram_id == message.id).first()

    if not result:
        return message.first_name
    return result.fullname


async def wk(mon: list, first_day: str):
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    tz_Moscow = pytz.timezone('Europe/Moscow')
    m = datetime.now(tz=tz_Moscow).month
    y = datetime.now(tz=tz_Moscow).year

    week = []

    last_month_date = int(months[m])

    if first_day == 'Mon':
        for _ in range(7):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}"))
        return week, 8
    elif first_day == 'Tue':

        week.append(InlineKeyboardButton(text=f"{last_month_date}", callback_data="data"))
        for _ in range(1, 6):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}"))
        return week, 7
    elif first_day == 'Wed':
        week.append(InlineKeyboardButton(text=f"{last_month_date}", callback_data="data"))
        for _ in range(1, 5):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}"))
        return week, 6
    elif first_day == 'Thu':
        week.append(InlineKeyboardButton(text=f"{last_month_date - 1}", callback_data="data"))
        week.append(InlineKeyboardButton(text=f"{last_month_date}", callback_data="data"))
        for _ in range(1, 4):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}"))
        return week, 5
    elif first_day == 'Fri':
        week.append(InlineKeyboardButton(text=f"{last_month_date - 2}", callback_data="data"))
        week.append(InlineKeyboardButton(text=f"{last_month_date - 1}", callback_data="data"))
        week.append(InlineKeyboardButton(text=f"{last_month_date}", callback_data="data"))
        for _ in range(1, 3):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}"))
        return week, 4
    elif first_day == 'Sat':
        week.append(InlineKeyboardButton(text=f"{last_month_date - 4}", callback_data="data"))
        week.append(InlineKeyboardButton(text=f"{last_month_date - 3}", callback_data="data"))
        week.append(InlineKeyboardButton(text=f"{last_month_date - 2}", callback_data="data"))
        week.append(InlineKeyboardButton(text=f"{last_month_date - 1}", callback_data="data"))
        week.append(InlineKeyboardButton(text=f"{last_month_date}", callback_data="data"))
        for _ in range(1, 2):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}"))
        return week, 3
    elif first_day == 'Sun':

        mon.append([InlineKeyboardButton(text=f"{last_month_date - 5}", callback_data="data"),
                    InlineKeyboardButton(text=f"{last_month_date - 4}", callback_data="data"),
                    InlineKeyboardButton(text=f"{last_month_date - 3}", callback_data="data"),
                    InlineKeyboardButton(text=f"{last_month_date - 2}", callback_data="data"),
                    InlineKeyboardButton(text=f"{last_month_date - 1}", callback_data="data"),
                    InlineKeyboardButton(text=f"{last_month_date}", callback_data="data"),
                    InlineKeyboardButton(text=f"1", callback_data=f"1")])
        return mon, 2
