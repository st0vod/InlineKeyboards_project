from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon_ru import LEXICON_RU_INLINEBUTTONS


url_buttons = [InlineKeyboardButton(text=text,
                                    url=url) for text, url in LEXICON_RU_INLINEBUTTONS.items()]

keyboard_inline = InlineKeyboardMarkup(inline_keyboard=[url_buttons])

