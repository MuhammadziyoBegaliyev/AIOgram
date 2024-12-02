from aiogram.utils.keyboard import ReplyKeyboardBuilder,KeyboardButton


builder = ReplyKeyboardBuilder()
builder.button(text="1-tugma")
builder.button(text="2-tugma")
builder.row(
    KeyboardButton(text="3-tugma"),
    KeyboardButton(text="4-tugma"),
    KeyboardButton(text="5-tugma"),
    KeyboardButton(text="6-tugma"),
    KeyboardButton(text="7-tugma"),
    KeyboardButton(text="8-tugma"),
    width=4
)
# builder.add(
#     KeyboardButton(text="3-tugma"),
#     KeyboardButton(text="4-tugma"),
#     KeyboardButton(text="5-tugma"),
#     KeyboardButton(text="6-tugma"), 
#     )



builder = builder.as_markup()
builder.resize_keyboard =True
builder.is_persistent =True