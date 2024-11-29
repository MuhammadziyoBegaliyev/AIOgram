from aiogram.types import Message
from aiogram import Bot
from aiogram.fsm.context import FSMContext

async def start_command_answer(message: Message, bot : Bot):
    await message.answer("Assalomu aleykum botdan foydala olmasangiz /help buyrugini yuboring.")


async def help_command_answer(message: Message,bot: Bot):
    matn = """Botdan foydalanish:
    /new - yangi ariza yuborish
    /stop-joriy arizani bekor qilish
    """
    await message.answer(matn)