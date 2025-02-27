from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU_INLINEBUTTONS

# ----- инлайн клавиатура с атрибутом url
url_buttons = [[InlineKeyboardButton(text=text,
                                    url=url)] for text, url in LEXICON_RU_INLINEBUTTONS.items()]

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=url_buttons)


# ----- инлайн клавиатура с атрибутом callback
callback_button_1 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 1',
    callback_data='callback_button_1_pressed')
callback_button_2 = InlineKeyboardButton(
    text='БОЛЬШАЯ КНОПКА 2',
    callback_data='callback_button_2_pressed')

keyboard_inline_callback = InlineKeyboardMarkup(
    inline_keyboard=[[callback_button_1],
                     [callback_button_2]]
)
