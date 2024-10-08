from aiogram import Router, F
from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery
)


router = Router()


@router.callback_query(F.data == 'tests_and_exams')
async def test_and_exams(call: CallbackQuery):
    await call.message.edit_text('1. Большие данные, вид оценивания: зачёт.\n\n'
    '2. Схемотехника электронных устройств, вид оценивания: экзамен.\n\n'
    '3. Системы автоматизированного проектирования конструкций радиоэлектронных средств, вид оценивания: экзамен, курсовая работа.\n\n'
    '4. Алгоритмическое обеспечение систем автоматизированного проектирования радиоэлектронных средств, вид оценивания: экзамен.\n\n' 
    '5. Иерархическое проектирование базовых несущих конструкций радиоэлектронных средств, вид оценивания: экзамен.\n\n' 
    '6. Параметрическая идентификация конструкций радиоэлектронных средств, вид оценивания: зачёт.\n\n' 
    '7. Проектирование систем охлаждения конструкций радиоэлектронных средств, вид оценивания: зачёт.  (по выбору)\n\n'
    '8. Создание специализированных систем в корпусе и систем на кристалле, вид оценивания: зачёт.  (по выбору)', reply_markup=InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Назад", callback_data="back")]
        ]
    ))