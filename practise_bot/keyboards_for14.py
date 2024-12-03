from aiogram.utils.keyboard import InlineKeyboardBuilder
from calendar import Calendar
inline_builder = InlineKeyboardBuilder()
kalendar = Calendar().itermonthdays2(2024,2)
for i in ("Du","Se","Cho","Pay","Ju","Sha","Yak"):
    inline_builder.button(text=i, callback_data=i)

for i in kalendar :
    if i[0]:inline_builder.button(text=f"{i[0] :02}", callback_data=f"{i[0] :02}")
    else : inline_builder.button(text="  ",callback_data="null")
inline_builder.adjust(7,repeat=True)
inline_builder = inline_builder.as_markup()