from aiogram import Bot , Dispatcher
from asyncio import run 
from aiogram.types import BotCommand
from aiogram.filters import Command
import funksiya
dp = Dispatcher()
async def startup_answer(bot: Bot):
    await bot.send_message(6824528065,  "Bot ishga tushurildi! ✅")


async def shutdown_answer(bot: Bot):
    await bot.send_message(6824528065,  "Bot To`xtatildi! ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.message.register(funksiya.start_command_answer, Command("start",prefix="/!"))
    dp.message.register(funksiya.help_command_answer,Command("help"))
    dp.shutdown.register(shutdown_answer)
    bot = Bot("7682918479:AAFIwfOI81ESlA1-KkZDyiueKX3_YrgL2Ik")
    await dp.start_polling(bot, polling_timeout=1)
    await bot.set_my_commands([
        BotCommand(command="/new", description="yangi ariza yuborish"),
        BotCommand(command="/stop",description="Arizani bekor qilish"),
        BotCommand(command="/help",description="Bo`tdan foydalaninshda yordam ")
    ])

run(start())
