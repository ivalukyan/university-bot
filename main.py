
import asyncio
import logging
import sys

from env import Telegram
from utils.utils import check_telegram_ids, time_for_dialog

from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, WebAppInfo, CallbackQuery
)

from tasks.tasks import router as task_router
from profiles.profile import router as profile_router
from admin import admin

from utils.utils import insert_info_abt_users, fullname


telegram = Telegram()
router = Router()
bot = Bot(token=telegram.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@router.message(CommandStart())
async def command_start(message: Message) -> None:

    if not str(message.from_user.id) in telegram.admins:
        await insert_info_abt_users(fullname=message.from_user.first_name, telegram_id=message.from_user.id,
                                     username=message.from_user.username)

    if await check_telegram_ids(message.from_user.id) or (str(message.from_user.id) in telegram.admins):
        await message.answer(f"{await time_for_dialog()}, {await fullname(message.from_user)}!\n\n<b><i>Created by @ivalkn</i></b>",
                              reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="👤 Профиль", callback_data="profile")],
            [InlineKeyboardButton(text="📅 Задания", callback_data="tasks")],
            [InlineKeyboardButton(text="🗂 Файлообменник", web_app=WebAppInfo(url="https://disk.yandex.ru/d/CVeZ-lzETYnsuw"))]
        ]))
    else:
        await message.answer(text="У вас нет доступа к данному боту")


async def main():
    # Initialize Bot instance with default bot properties which will be passed to all API calls

    dp.include_routers(router, task_router, admin.router, profile_router)

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
