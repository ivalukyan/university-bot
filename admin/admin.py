from env import Telegram

from aiogram import Router, html, F
from aiogram.filters import Command
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, 
    CallbackQuery
)
from aiogram.types import FSInputFile
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

from main import bot

from database.db import Session, User

telegram = Telegram()
router = Router()


class Form(StatesGroup):
    """
    req_adm - state for send messages from users
    """

    # Admin
    mailing = State()


@router.message(Command("admin"))
async def command_admin(message: Message) -> None:

    if str(message.from_user.id) in telegram.admins:
        await message.answer(
            f"Здравствуйте, {html.quote(message.from_user.first_name)},"
            f" чтобы прейти в приложение Web App, нажмите кнопку\n\n<b><i>Created by @ivalkn</i></b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='University App', url=f"{telegram.url}")],
                [InlineKeyboardButton(text="Рассылка", callback_data='mailing')],
                [InlineKeyboardButton(text="ID пользователей", callback_data='file')]
            ]),
        )
    else:
        await message.answer("У вас нет доступа к данному меню")


@router.callback_query(F.data == "mailing")
async def mailing(call: CallbackQuery, state: FSMContext) -> None:

    db_session = Session()
    telegram_ids = db_session.query(User.telegram_id).all()

    if not telegram_ids:
        await call.message.edit_text("Пользоватлей нет в БД", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="back_to_admin")]
            ]
        ))
    else:
        await state.set_state(Form.mailing)
        await call.message.edit_text("Введите сообщение для рассылки: ", reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text="Назад", callback_data="back_to_admin")]
            ]
        ))


@router.message(Form.mailing)
async def mailing(message: Message, state: FSMContext) -> None:

    db_session = Session()
    telegram_ids = db_session.query(User.telegram_id).all()
    ids = [_[0] for _ in telegram_ids]

    for _ in ids:
        await bot.send_message(_, message.text)
    await state.clear()


@router.callback_query(F.data == "back_to_admin")
async def back_to_admin_panel(call: CallbackQuery) -> None:
        await call.message.edit_text(
            f"Здравствуйте, {html.quote(call.message.chat.first_name)},"
            f" чтобы прейти в приложение Web App, нажмите кнопку\n\n<b><i>Created by @ivalkn</i></b>",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='University App', url=f"{telegram.url}")],
                [InlineKeyboardButton(text="Рассылка", callback_data='mailing')],
                [InlineKeyboardButton(text="ID пользователей", callback_data='file')]
            ]),
        )


@router.callback_query(F.data == "file")
async def file(call: CallbackQuery) -> None:
    await call.message.answer_document(document=FSInputFile('files/users.xlsx'))
