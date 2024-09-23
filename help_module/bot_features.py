from aiogram import Router, F
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery
)


router = Router()


@router.callback_query(F.data == 'bot_features')
async def test_and_exams(call: CallbackQuery):
    await call.message.edit_text('<b>Раздел <i>👤 Профиль</i></b>\n\n'
                                 '<b><i>СДО</i></b> - здесь вы можете быстро перейти на сдо в свой личный кабинет\n'
                                 '<b><i>Сканер QR</i></b> - возможность быстро отметиться на паре просто отсканировав QR\n\n'
                                 '<b>Раздел <i>📚 Предметы</i></b>\n\n'
                                 'Здесь вы сможете выбрав нужный предмет получить информацию или записаться для сдачи презентаций'
                                 '<b>Раздел <i>📅 Задания</i></b>\n\n'
                                 'Здесь вы сможете посмотреть задания или дедлайны сдачи работ по разным предметам\n\n'
                                 '<b>Раздел <i>📒 Зачеты/Экзамены</i></b>\n\n'
                                 'Здесь вы сможете посмотреть информацию о зачетах/экзаменах по предметам\n\n'
                                 '<b>Раздел <i>🗂 Файлообменник</i></b>\n\n'
                                 'Здесь вы сможете найти файлы практических, лекций, лабораторных по разным предметам',
                                   reply_markup=InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back")]
        ]
    ))