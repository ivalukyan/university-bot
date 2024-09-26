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
            [InlineKeyboardButton(text="💻 Темы курсовых, докладов", callback_data="subjects")],
            [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]))


@router.callback_query(F.data == 'subjects')
async def view_subjects(call: CallbackQuery):
    await call.message.edit_text("Предметы\n\n ‼️ Чтобы на телефоне изменить файл нужны Google Документы, Google Таблицы.\n"
                                 "Для айфонов нужно нажать справа внизу на иконку сафари после того как нажали кнопку.‼️",
                                  reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📕 САПР", url="https://clck.ru/3DMcY9")],
            [InlineKeyboardButton(text="📗 Социальная педагогика", url="https://clck.ru/3DTbH6")],
            [InlineKeyboardButton(text="📙 Системы на кристалле", url="https://clck.ru/3DXgPD")],
            [InlineKeyboardButton(text="Назад", callback_data="back_for_subjects")]
        ]
    ))


@router.callback_query(F.data == "back_for_subjects")
async def back_for_subjects(call: CallbackQuery):
        await call.message.edit_text(f"🗓 <b><i>Профиль студента</i></b> <i>{await fullname(call.message.chat)}</i> 🗓", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🖥 СДО", web_app=WebAppInfo(url="https://online-edu.mirea.ru/login/"))],
            [InlineKeyboardButton(text="📸 Сканер QR ", web_app=WebAppInfo(url="https://attendance-app.mirea.ru/selfapprove"))],
            [InlineKeyboardButton(text="💻 Темы курсовых, докладов", callback_data="subjects")],
            [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]))