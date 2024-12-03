from aiogram.types import CallbackQuery
async def ok_answer(CallBackData: CallbackQuery):
    await CallBackData.answer('Xabar ochirildi', show_alert= True)
    await CallBackData.message.delete()
    