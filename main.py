
import asyncio
import logging
import sys

from env import Telegram
from utils.utils import check_telegram_ids, time_for_dialog

from aiogram import Bot, Dispatcher, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, WebAppInfo,
)

from tasks.tasks import router as task_router
from profiles.profile import router as profile_router


telegram = Telegram()
router = Router()


@router.message(CommandStart())
async def command_start(message: Message) -> None:

    if await check_telegram_ids(message.from_user.id):
        await message.answer(f"{await time_for_dialog()}, {message.from_user.first_name}",
                              reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Профиль", callback_data="profile")],
            [InlineKeyboardButton(text="Задания", callback_data="tasks")],
            [InlineKeyboardButton(text="Файлобменник", web_app=WebAppInfo(url="https://disk.yandex.ru/d/CVeZ-lzETYnsuw"))]
        ]))
    else:
        await message.answer(text="У вас нет доступа к данному боту")


@router.message(Command("admin"))
async def command_admin(message: Message) -> None:

    if str(message.from_user.id) in telegram.admins:
        await message.answer(
            f"Здравствуйте, {html.quote(message.from_user.first_name)},"
            f" чтобы прейти в приложение Web App, нажмите кнопку",
            reply_markup=InlineKeyboardMarkup(inline_keyboard=[
                [InlineKeyboardButton(text='University App', url=f"{telegram.url}")]
            ]),
        )
    else:
        await message.answer("У вас нет доступа к данному меню")


async def main():
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=telegram.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.include_routers(router, task_router, profile_router)

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
