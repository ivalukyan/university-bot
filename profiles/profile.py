from aiogram import Bot, Dispatcher, Router, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, WebAppInfo, CallbackQuery
)


router = Router()


@router.callback_query(F.data == "profile")
async def read_profile(call: CallbackQuery) -> None:
    await call.message.edit_text("<b><i>ПРОФИЛЬ</i></b>", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="СДО", web_app=WebAppInfo(url="https://online-edu.mirea.ru/login/"))],
            [InlineKeyboardButton(text="Сканер QR ", web_app=WebAppInfo(url="https://attendance-app.mirea.ru/selfapprove"))],
            [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]))