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
            [InlineKeyboardButton(text="📚 Предметы", callback_data="subjects")],
            [InlineKeyboardButton(text="🔗 Темы для курсовой", web_app=WebAppInfo(url="https://clck.ru/3DMcY9"))],
            [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]))


@router.callback_query(F.data == 'subjects')
async def view_subjects(call: CallbackQuery):
    await call.message.edit_text("Предметы", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📕 САПР Констр. РС", callback_data="sapr")],
            [InlineKeyboardButton(text="📗 Социальная пед. и психол.", callback_data="pedagogy")],
            [InlineKeyboardButton(text="Назад", callback_data="back_for_subjects")]
        ]
    ))


@router.callback_query(F.data == "pedagogy")
async def pedagogy(call: CallbackQuery):
      await call.message.edit_text("Социяльная психология и педагогика", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                  [InlineKeyboardButton(text="Темы презентаций", web_app=WebAppInfo(url="https://clck.ru/3DTVVa"))],
                  [InlineKeyboardButton(text="Назад", callback_data="back_to_subject")]
            ]
      ))


@router.callback_query(F.data == "sapr")
async def capr(call: CallbackQuery):
     await call.message.edit_text("САПР конструкций радиоэлектронных средств", reply_markup=InlineKeyboardMarkup(
          inline_keyboard=[
               [InlineKeyboardButton(text="✏️ Темы для курсовой", web_app=WebAppInfo(url="https://clck.ru/3DMcY9"))],
               [InlineKeyboardButton(text="Назад", callback_data="back_to_subject")]
          ]
     ))


@router.callback_query(F.data == "back_to_subject")
async def back_to_subjects(call: CallbackQuery):
         await call.message.edit_text("Предметы", reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="📕 САПР Констр. РС", callback_data="sapr")],
            [InlineKeyboardButton(text="📗 Социальная пед. и психол.")],
            [InlineKeyboardButton(text="Назад", callback_data="back_for_subjects")]
        ]
    ))


@router.callback_query(F.data == "back_for_subjects")
async def back_for_subjects(call: CallbackQuery):
        await call.message.edit_text(f"🗓 <b><i>Профиль студента</i></b> <i>{await fullname(call.message.chat)}</i> 🗓", reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🖥 СДО", web_app=WebAppInfo(url="https://online-edu.mirea.ru/login/"))],
            [InlineKeyboardButton(text="📸 Сканер QR ", web_app=WebAppInfo(url="https://attendance-app.mirea.ru/selfapprove"))],
            [InlineKeyboardButton(text="📚 Предметы", callback_data="subjects")],
            [InlineKeyboardButton(text="🔗 Темы для курсовой", web_app=WebAppInfo(url="https://clck.ru/3DMcY9"))],
            [InlineKeyboardButton(text="Назад", callback_data="back")]
    ]))