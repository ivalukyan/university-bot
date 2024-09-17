from aiogram import Bot, Dispatcher, Router, html, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, WebAppInfo, CallbackQuery
)

from utils.utils import fullname


router = Router()


@router.callback_query(F.data == "profile")
async def read_profile(call: CallbackQuery) -> None:
    await call.message.edit_text(f"🗓 <b><i>Профиль студента</i></b> <i>{await fullname(call.message.chat)}</i> 🗓", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🖥 СДО", web_app=WebAppInfo(url="https://online-edu.mirea.ru/login/"))],
            [InlineKeyboardButton(text="📸 Сканер QR ", web_app=WebAppInfo(url="https://attendance-app.mirea.ru/selfapprove"))],
            [InlineKeyboardButton(text="🔗 Темы для курсовой", web_app=WebAppInfo(url="https://clck.ru/3DMcY9"))],
            [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]))