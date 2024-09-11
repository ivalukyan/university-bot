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
from utils.utils import create_calandar, check_telegram_ids, time_for_dialog

router = Router()


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

    if await check_telegram_ids(call.message.chat.id):
        await call.message.edit_text(f"{await time_for_dialog()}, {call.message.chat.first_name}", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Профиль", callback_data="profile")],
            [InlineKeyboardButton(text="Задания", callback_data="tasks")],
            [InlineKeyboardButton(text="Файлобменник", web_app=WebAppInfo(url="https://disk.yandex.ru/d/CVeZ-lzETYnsuw"))]
        ]))
    else:
        await call.message.edit_text(text="У вас нет доступа к данному боту")