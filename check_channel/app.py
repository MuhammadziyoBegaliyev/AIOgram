import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from utils import get_channels_ikb
from aiogram import types, Bot ,F

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "7682918479:AAFIwfOI81ESlA1-KkZDyiueKX3_YrgL2Ik"    

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(
        text = 'Follow to Continue',
        reply_markup= get_channels_ikb()
    )



@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


@dp.callback_query(F.data == 'check_follow')
async def check_follow(cb: types.CallbackQuery, bot: Bot):

    result = await bot.get_chat_member(
        chat_id=-1002258706964,
        user_id=cb.from_user.id
    )
    print(result)

    if result.status in ['creator','administrator','member']:
        await cb.answer("You are subscribed")
    
    else:
        await cb.answer(
            text='You are not subscribed'
        )
        return

    await cb.message.edit_text(
        text ='You are subscribed'
    )


async def main() -> None:
    bot = Bot(token=TOKEN)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())