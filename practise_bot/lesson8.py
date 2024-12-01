from aiogram import Bot, Dispatcher ,F
from asyncio import run
import funksiyalar

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(6824528065, 'Bot ishga tushdi !')

async def shutdown_answer(bot:Bot):
    await bot.send_message(6824528065, 'Bot ishdan to`qtadi!')

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(funksiyalar.cancel_markup, F.text.lower()== 'cancel')
    dp.message.register(funksiyalar.qandaydur_answer)

    bot = Bot('7975356285:AAEtEG5Hi1KOXB4xko2np2R0Bt3mYnkgCEQ')
    await dp.start_polling(bot, polling_timeout=1)


run(start())