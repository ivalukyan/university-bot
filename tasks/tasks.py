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


@router.callback_query(F.data == "tasks")
async def tasks(call: CallbackQuery) -> None:

    tz_Moscow = pytz.timezone('Europe/Moscow')
    date = datetime.now(tz=tz_Moscow).strftime("%d-%m-%Y")
    m = datetime.now(tz=tz_Moscow).month

    keyboard = await create_calandar(m)

    await call.message.edit_text(text=f"Выберите дату, Сегодня: {html.italic(html.bold(date))}",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=keyboard))
    

@router.callback_query(F.data == "back")
async def back(call: CallbackQuery) -> None:

    if await check_telegram_ids(call.message.chat.id) or (str(call.message.chat.id) in telegram.admins):
        await call.message.edit_text(f"{await time_for_dialog()}, {await fullname(call.message.chat)}!\n\n<b><i>Created by @ivalkn</i></b>", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Профиль", callback_data="profile")],
            [InlineKeyboardButton(text="Задания", callback_data="tasks")],
            [InlineKeyboardButton(text="Файлобменник", web_app=WebAppInfo(url="https://disk.yandex.ru/d/CVeZ-lzETYnsuw"))]
        ]))
    else:
        await call.message.edit_text(text="У вас нет доступа к данному боту")


@router.callback_query(F.data == "1")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))


@router.callback_query(F.data == "2")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))


@router.callback_query(F.data == "3")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))


@router.callback_query(F.data == "4")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "5")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "6")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))


@router.callback_query(F.data == "7")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "8")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "9")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))


@router.callback_query(F.data == "10")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "11")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "12")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "13")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "14")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "15")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "16")
async def day_info(call: CallbackQuery) -> None:

    tz_Moscow = pytz.timezone('Europe/Moscow')
    y = datetime.now(tz=tz_Moscow).year
    m = str(datetime.now(tz=tz_Moscow).month)
    d = call.data

    date = f'{numerals[d]}-{numerals[m]}-{y}'

    db_session = Session()
    text = db_session.query(Task).filter(Task.date == date).all()

    if not text:
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "17")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "18")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "19")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "20")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "21")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "22")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "23")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "24")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "25")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "26")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))


@router.callback_query(F.data == "27")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))


@router.callback_query(F.data == "28")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "29")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))


@router.callback_query(F.data == "30")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))



@router.callback_query(F.data == "31")
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
        await call.message.edit_text("Здание отсутствует", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))
    else:
        msg = ""
        for _ in text:
            msg += f"<b>Предмет:</b> {_.subject}\n<b>Тип:</b> {_.type}\n<b>Задание</b>: {_.task}\n\n"

        await call.message.edit_text(msg,
                                      reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="tasks")]
            ]
        ))

