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
    for channel in channel_list:
        channel_name = f'@{channel[13:]}'
        
        member = await bot.get_chat_member(
            chat_id= channel_name,
            user_id= cb.from_user.id
        )

        if member.status not in ['creator','administrator','member']:
            await cb.answer(
                text= 'You are not subscribed'
            )
            return
        else:
            await cb.message.edit_text(
                text ='You are subscribed'
            )



async def ok_answer(CallBackData: CallbackQuery):
    await CallBackData.answer('Azo bo`ldingiz', show_alert= True)
    await CallBackData.message.delete()
    