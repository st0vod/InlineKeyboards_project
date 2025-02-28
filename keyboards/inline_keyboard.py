from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
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

# ----- билдер Inline клавиатуры
inline_kb_builder = InlineKeyboardBuilder()

buttons: list[InlineKeyboardButton] = [InlineKeyboardButton(text=f'{i}', callback_data=f'{i}') for i in range(1, 11)]

inline_kb_builder.add(*buttons)
inline_kb_builder.adjust(5, repeat=True)

kb_builder = inline_kb_builder.as_markup(resize_keybord=True)