from aiogram.utils.keyboard import InlineKeyboardBuilder

# 7 8 9 +
# 4 5 6 - 
# 1 2 3 *    >>> kalkulyator ko`riniishi`
# , 0 / = 

calc_builder = InlineKeyboardBuilder()
for i in "789+456-123*,0/=":
    calc_builder.button(text=i,callback_data=i)
calc_builder.adjust(4, repeat= True)
calc_builder = calc_builder.as_markup