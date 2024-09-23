import pytz

from aiogram import Bot, Dispatcher, Router, F, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, WebAppInfo, CallbackQuery
)

from datetime import datetime
from utils.utils import create_calandar, check_telegram_ids, time_for_dialog, fullname
from database.db import Session, Task
from utils.translations import numerals
from env import Telegram

router = Router()
telegram = Telegram()
dates = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10',
          '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
          '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'}


@router.callback_query(F.data == "tasks")
async def tasks(call: CallbackQuery) -> None:

    tz_Moscow = pytz.timezone('Europe/Moscow')
    date = datetime.now(tz=tz_Moscow).strftime("%d-%m-%Y")
    m = datetime.now(tz=tz_Moscow).month
    y = datetime.now(tz=tz_Moscow).year
    d = datetime.now(tz=tz_Moscow).day

    weeks = {'Mon': 'Пн', 'Tue': 'Вт', 'Wed': 'Ср', 'Thu': 'Чт', 'Fri': 'Пт', 'Sat': 'Сб', 'Sun': 'Вс'}

    keyboard = await create_calandar(m)

    await call.message.edit_text(text=f"Выберите дату, Сегодня: {html.italic(html.bold(date))} - "
                                 f"{html.italic(html.bold(weeks[datetime(y, m, d).strftime('%a')]))}",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard))
    

@router.callback_query(F.data == "back")
async def back(call: CallbackQuery) -> None:

    if await check_telegram_ids(call.message.chat.id) or (str(call.message.chat.id) in telegram.admins):
        await call.message.edit_text(f"{await time_for_dialog()}, {await fullname(call.message.chat)}!\n\n<b><i>Created by @ivalkn</i></b>", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
            [InlineKeyboardButton(text="📅 Задания", callback_data="tasks")],
            [InlineKeyboardButton(text="📒 Зачеты/Экзамены", callback_data="tests_and_exams")],
            [InlineKeyboardButton(text="📍 Возможности бота", callback_data="bot_features")],
            [InlineKeyboardButton(text="🗂 Файлообменник", web_app=WebAppInfo(url="https://disk.yandex.ru/d/CVeZ-lzETYnsuw"))]
        ]))
    else:
        await call.message.edit_text(text="У вас нет доступа к данному боту")


@router.callback_query(F.data.in_(dates))
async def day_info(call: CallbackQuery) -> None:

    tz_Moscow = pytz.timezone('Europe/Moscow')
    y = datetime.now(tz=tz_Moscow).year
    m = str(datetime.now(tz=tz_Moscow).month)
    d = call.data

    date = f'{numerals[d]}-{numerals[m]}-{y}'
    print(date)

    db_session = Session()
    text = db_session.query(Task).filter(Task.date == date).all()

    if not text:
        await call.message.edit_text("Задание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"🗂 <b>Предмет:</b> {_.subject}\n📒 <b>Тип:</b> {_.type}\n📌 <b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
