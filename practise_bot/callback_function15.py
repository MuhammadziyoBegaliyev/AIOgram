from aiogram.types import CallbackQuery

async def callback_answer(callback: CallbackQuery):
    if callback.message.text == "☎️":
        if callback.data in "0+-*/=,":
            await callback.answer(f"Siz ifodani {callback.data} buyrug`i boshlay olmaymiz",show_alert= True)
        else:
            await callback.message.edit_text(callback.data + callback.message.text)
    else:
        if callback.data == "=" and "+" in callable.message.text or "-" in callable.message.text or"*" in callable.message.text or "/" in callable.message.text :
            await callable.message.edit_text(
                str(eval(callback.message.text))
                )
        elif callback.data == "=":
            await callback_answer("ifoda to`liq emas", show_alert=True)
                
        elif callback.message.text[-2].isdigit():
            await callback.message.edit_text(
                callback.message.text[:-1]+ callback.data + callback.message.text[-1]
            )
       