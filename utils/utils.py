import pytz

from datetime import datetime


async def check_telegram_ids(user_id: int) -> bool:

    telegram_ids = [877008114]

    if user_id in telegram_ids:
        return True
    return False


async def time_for_dialog() -> str:

    tz_Moscow = pytz.timezone('Europe/Moscow')
    hour = datetime.now(tz=tz_Moscow).hour

    if hour in [18, 19, 20, 21, 22, 23, 0, 1, 2]:
        return "Добрый вечер"
    elif hour in [3, 4, 5, 6, 7, 8, 9, 10, 11]:
        return "Доброе утро"
    else:
        return "Добрый день"