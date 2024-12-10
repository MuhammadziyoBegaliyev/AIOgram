from aiogram.types import Message
import keyboards_for15
async def open_calc_answer(message: Message):
    await message.answer("|", reply_markup=keyboards_for15.calc_builder)