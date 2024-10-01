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
    cal_months = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь', 7: 'Июль',
                  8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}

    mon.append([InlineKeyboardButton(text=f"{cal_months[month]}", callback_data="mon")])

    mon.append([
        InlineKeyboardButton(text='Пн', callback_data='Mon'),
        InlineKeyboardButton(text='Вт', callback_data='Tue'),
        InlineKeyboardButton(text='Ср', callback_data='Wed'),
        InlineKeyboardButton(text='Чт', callback_data='Thu'),
        InlineKeyboardButton(text='Пт', callback_data='Fri'),
        InlineKeyboardButton(text='Сб', callback_data='Sat'),
        InlineKeyboardButton(text='Вс', callback_data='Sun')
    ])

    res = await wk(first_day=datetime(y, month, 1).strftime('%a'), m=month)

    day = res[1]

    mon.append(res[0])

    while day != months[month]:

        for _ in range(7):

            week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}-{month}-{y}"))

            day += 1

            if day == months[month]:

                if len(week) == 7:
                    mon.append(week)
                    week = []
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}-{month}-{y}"))
                    for _ in range(6):
                        week.append(InlineKeyboardButton(text=" ", callback_data="data"))
                    break
                elif len(week) == 6:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}-{month}-{y}"))
                    break
                elif len(week) == 5:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}-{month}-{y}"))
                    for _ in range(1):
                        week.append(InlineKeyboardButton(text=" ", callback_data="data"))
                    break
                elif len(week) == 4:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}-{month}-{y}"))
                    for _ in range(2):
                        week.append(InlineKeyboardButton(text=" ", callback_data="data"))
                    break
                elif len(week) == 3:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}-{month}-{y}"))
                    for _ in range(3):
                        week.append(InlineKeyboardButton(text=" ", callback_data="data"))
                    break
                elif len(week) == 2:
                    week.append(InlineKeyboardButton(text=f"{day}", callback_data=f"{day}-{month}-{y}"))
                    for _ in range(4):
                        week.append(InlineKeyboardButton(text=" ", callback_data="data"))
                    break                
                

        mon.append(week)
        week = []

    mon.append([InlineKeyboardButton(text="⬅️", callback_data="before_tasks"),
                InlineKeyboardButton(text="🏠", callback_data="tasks"),
                InlineKeyboardButton(text="➡️", callback_data="after_tasks")])
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


async def wk(first_day: str, m: str):
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    tz_Moscow = pytz.timezone('Europe/Moscow')
    # m = datetime.now(tz=tz_Moscow).month
    y = datetime.now(tz=tz_Moscow).year

    week = []

    if first_day == 'Mon':
        for _ in range(7):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}-{m}-{y}"))
        return week, 8
    elif first_day == 'Tue':

        week.append(InlineKeyboardButton(text=f" ", callback_data="data"))
        for _ in range(1, 7):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}-{m}-{y}"))
        return week, 7
    elif first_day == 'Wed':
        for _ in range(2):
            week.append(InlineKeyboardButton(text=f" ", callback_data="data"))
        for _ in range(1, 6):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}-{m}-{y}"))
        return week, 6
    elif first_day == 'Thu':
        for _ in range(3):
            week.append(InlineKeyboardButton(text=f"", callback_data="data"))
        for _ in range(1, 5):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}-{m}-{y}"))
        return week, 5
    elif first_day == 'Fri':
        for _ in range(4):
            week.append(InlineKeyboardButton(text=f" ", callback_data="data"))
        for _ in range(1, 4):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}-{m}-{y}"))
        return week, 4
    elif first_day == 'Sat':
        for _ in range(5):
            week.append(InlineKeyboardButton(text=f" ", callback_data="data"))
        for _ in range(1, 3):
            week.append(InlineKeyboardButton(text=f"{_}", callback_data=f"{_}-{m}-{y}"))
        return week, 3
    elif first_day == 'Sun':
        for _ in range(6):
            week.append(InlineKeyboardButton(text=f" ", callback_data="data"))
        week.append(InlineKeyboardButton(text="1", callback_data=f"1-{m}-{y}"))

        return week, 2

def genrate_dates() -> dict:
    tz_Moscow = pytz.timezone('Europe/Moscow')
    year = datetime.now(tz=tz_Moscow).year

    dates = []

    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    for i in range(1, 12+1):
        for y in range(1, months[i]+1):
            dates.append(f"{y}-{i}-{year}")

    # print(dates)

    return dates