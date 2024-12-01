from aiogram.types import ReplyKeyboardMarkup ,KeyboardButton

biror_bir_tugmalar = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='1-tugma'),
            KeyboardButton(text='2-tugma'),
            KeyboardButton(text='3-tugma')
         ],
         [
            KeyboardButton(text='4-tugma'),
            KeyboardButton(text='5-tugma'),
            KeyboardButton(text='6-tugma')  
         ]
         
    ],
    resize_keyboard=True, 
    #is_persistent=True    
    input_field_placeholder="Gullola Nasimova"
)