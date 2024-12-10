from aiogram import types, Bot, Router ,F
from aiogram.filters import Command
from aiogram.types import CallbackQuery

from joincode import get_channels_ikb ,channel_list
main_router = Router()


@main_router.message(Command("start"))
async def cmd_start(msg: types.Message):
    await msg.answer(
        text = 'Follow to Continue',
        reply_markup= get_channels_ikb()
    )


@main_router.callback_query(F.data == 'check_follow')
async def check_follow(cb: types.CallbackQuery, bot: Bot):

    status = await bot.get_chat_member(
        chat_id=-1002258706964,
        user_id=cb.from_user.id
    )

    if status in ['creator','administrator','member']:
        await cb.answer("You are subscribed")
    
    else:
        await cb.answer(
            text='You are not subscribed'
        )
        await cb.message.edit_text(
            text ='You are subscribed'
        )


async def ok_answer(CallBackData: CallbackQuery):
    await CallBackData.answer('Azo bo`ldingiz', show_alert= True)
    await CallBackData.message.delete()
