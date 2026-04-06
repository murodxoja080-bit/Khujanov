from aiogram.utils.keyboard import InlineKeyboardBuilder

def premium_builder(buttons_dict: dict, sizes: list):
    builder = InlineKeyboardBuilder()
    for text, data in buttons_dict.items():
        builder.button(text=text, callback_data=data)
    builder.adjust(*sizes)
    return builder.as_markup()
