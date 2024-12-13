from aiogram.client.session.aiohttp import AiohttpSession
from aiogram import Bot, Dispatcher, F
from aiogram.filters import and_f
from asyncio import run 
import function_for17

dp = Dispatcher()

async def startup_answer(bot:Bot):
    await bot.send_message(6824528065, "Bot ihga tushdi ✅")

async def shutdown_answer(bot:Bot):
    await bot.send_message(6824528065, "Bot ishdan toxtadi ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(function_for17.new_chat_members_answer, and_f(F.chat.type == "supergroup", F.new_chat_members))
    dp.message.register(function_for17.left_chat_member_answer, and_f(F.chat.type == "Supergroup" , F.left_chat_member))
    bot = Bot ("7843936213:AAERyf2jk-oAypnim4bIqMB3Kch5agz-_pQ")
    await dp.start_polling(bot, polling_timeout=1)


run(start())

