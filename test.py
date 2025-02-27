from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from configs.config import load_config, Config

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
config: Config = load_config()

# Создаем объекты бота и диспетчера
bot = Bot(token=config.tg_bot.token)
dp = Dispatcher()

# Создаем объекты инлайн-кнопок
group_name = 'aiogram_stepik_course'
url_button_1 = InlineKeyboardButton(
    text='Группа "Телеграм-боты на AIOgram"',
    url=f'tg://resolve?domain={group_name}'
)
user_id = 173901673
url_button_2 = InlineKeyboardButton(
    text='Автор курса на Степике по телеграм-ботам',
    url=f'tg://user?id={user_id}'
)

channel_name = 'toBeAnMLspecialist'
url_button_3 = InlineKeyboardButton(
    text='Канал "Стать специалистом по машинному обучению"',
    url=f'https://t.me/{channel_name}'
)

# Создаем объект инлайн-клавиатуры
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[url_button_1],
                     [url_button_2],
                     [url_button_3]]
)


# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру c url-кнопками
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text='Это инлайн-кнопки с параметром "url"',
        reply_markup=keyboard
    )


if __name__ == '__main__':
    dp.run_polling(bot)