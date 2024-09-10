from aiogram import Bot, Dispatcher, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, WebAppInfo, CallbackQuery
)


router = Router()


@router.callback_query(F.data == "tasks")
async def tasks(call: CallbackQuery) -> None:
    await call.message.edit_text(text="Выберите дату", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="1", callback_data="1"), InlineKeyboardButton(text="2", callback_data="2"),
        InlineKeyboardButton(text="3", callback_data="3"), InlineKeyboardButton(text="4", callback_data="4"),
        InlineKeyboardButton(text="5", callback_data="5"), InlineKeyboardButton(text="6", callback_data="6"),
        InlineKeyboardButton(text="7", callback_data="7")],
        [InlineKeyboardButton(text="8", callback_data="8"), InlineKeyboardButton(text="9", callback_data="9"),
        InlineKeyboardButton(text="10", callback_data="10"), InlineKeyboardButton(text="11", callback_data="11"),
        InlineKeyboardButton(text="12", callback_data="13"), InlineKeyboardButton(text="14", callback_data="15"),
        InlineKeyboardButton(text="16", callback_data="16")],
        [InlineKeyboardButton(text="17", callback_data="17"), InlineKeyboardButton(text="18", callback_data="18"),
        InlineKeyboardButton(text="19", callback_data="19"), InlineKeyboardButton(text="20", callback_data="20"),
        InlineKeyboardButton(text="21", callback_data="21"), InlineKeyboardButton(text="22", callback_data="22"),
        InlineKeyboardButton(text="23", callback_data="23")],
        [InlineKeyboardButton(text="24", callback_data="24"), InlineKeyboardButton(text="25", callback_data="25"),
        InlineKeyboardButton(text="26", callback_data="26"), InlineKeyboardButton(text="27", callback_data="27"),
        InlineKeyboardButton(text="28", callback_data="28"), InlineKeyboardButton(text="29", callback_data="29"),
        InlineKeyboardButton(text="30", callback_data="30")],
        [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]))