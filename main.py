
import asyncio
import logging
import sys
from env import Telegram

from aiogram import Bot, Dispatcher, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import (
    InlineKeyboardButton,
    Message,
    InlineKeyboardMarkup, WebAppInfo,
)

telegram = Telegram()
router = Router()


@router.message(CommandStart())
async def command_start(message: Message) -> None:
    await message.answer(
        f"Здравствуйте, {html.quote(message.from_user.first_name)},"
        f" чтобы прейти в приложение Web App, нажмите кнопку",
        reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text='University App', url=f"{telegram.url}")]
        ]),
    )


async def main():
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=telegram.token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()

    dp.include_router(router)

    # Start event dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
