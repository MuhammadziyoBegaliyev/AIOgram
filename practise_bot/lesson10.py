from aiogram import Bot, Dispatcher, F
from asyncio import run
from aiogram.filters import CommandStart
import function_for10

dp = Dispatcher()

async def startup_answer(bot:Bot):
    await bot.send_message(6824528065,"Bot ishga tushdi😍")

async def shutdown_answer(bot :Bot):
    await bot.send_message(6824528065, "Bot ishdan toqtadi ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(function_for10.start_command_reply,CommandStart())
    dp.message.register(function_for10.get_contact_info, F.contact)
    dp.message.register(function_for10.get_locatio_info, F.location)
    bot = Bot("7975356285:AAEtEG5Hi1KOXB4xko2np2R0Bt3mYnkgCEQ")
    await dp.start_polling(bot, polling_timeout=1)

run(start())