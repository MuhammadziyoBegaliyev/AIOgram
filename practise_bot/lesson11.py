from aiogram import Bot, Dispatcher, F
from asyncio import run 
import function11
import filters11

dp = Dispatcher()

async def startup_answer(bot: Bot):
    await bot.send_message(6824528065,"Bot ishga tushdi😍")

async def shutdown_answer(bot :Bot):
    await bot.send_message(6824528065, "Bo`t ishdan to`xtadi!")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(function11.sub_channel_answer,filters11.CheckSubChannel())
    dp.message.register(function11.get_channel_id_answer, F.forward_from_chat)
    dp.message.register(function11.echo)

    bot = Bot("7682918479:AAFIwfOI81ESlA1-KkZDyiueKX3_YrgL2Ik")
    await dp.start_polling(bot, polling_timeout=1)

run(start())