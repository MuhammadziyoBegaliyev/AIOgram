from aiogram import Bot, Dispatcher , F
from asyncio import run 
from aiogram.filters import and_f
from aiogram.client.session.aiohttp import AiohttpSession
import function_for18


dp = Dispatcher()

async def startup_answer(bot:Bot):
    await bot.send_message(6824528065, "Bot ihga tushdi ✅")

async def shutdown_answer(bot:Bot):
    await bot.send_message(6824528065, "Bot ishdan toxtadi ❌")

async def start():
    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)
    dp.message.register(function_for18.new_chat_members_answer, and_f(F.chat.id == -1002236343456, F.new_chat_members))
    dp.message.register(function_for18.left_chat_member_answer, and_f(F.chat.id == -1002236343456, F.left_chat_member))
    dp.message.register(function_for18.mute_member_answer, and_f(F.chat.type == "supergroup", and_f(F.text == "/mute", F.reply_to_message)))
    dp.message.register(function_for18.unban_member_answer, and_f(F.chat.type == "supergroup", and_f(F.text == "/unmute", F.reply_to_message)))
    dp.message.register(function_for18.ban_member_answer, and_f(F.chat.type == "supergroup", and_f(F.text == "/ban", F.reply_to_message)))
    dp.message.register(function_for18.unban_member_answer, and_f(F.chat.type == "supergroup", and_f(F.text == "/unban", F.reply_to_message)))

    bot = Bot("7843936213:AAERyf2jk-oAypnim4bIqMB3Kch5agz-_pQ")
    await dp.start_polling(bot, polling_timeout=1)

run(start())