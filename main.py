import data
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# Инициализация бота и диспетчера
bot_token = data.TOKEN
bot = Bot(token=bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


# Определение функции обратного вызова для обработки нажатий на кнопки с вопросами
@dp.callback_query_handler(lambda c: c.data.startswith('question_'))
async def process_question_callback(callback_query: types.CallbackQuery):
    question_number = callback_query.data.split('_')[1]  # Получение номера вопроса из данных обратного вызова

    # Отправка соответствующего текстового сообщения в зависимости от номера вопроса
    if question_number == '1':
        await bot.send_message(callback_query.from_user.id, data.l1, disable_web_page_preview=False)
    elif question_number == '2':
        await bot.send_message(callback_query.from_user.id, data.l2, disable_web_page_preview=False)
    elif question_number == '3':
        await bot.send_message(callback_query.from_user.id, data.l3, disable_web_page_preview=False)
    elif question_number == '4':
        await bot.send_message(callback_query.from_user.id, data.l4, disable_web_page_preview=False)


# Обработка команды /start
@dp.message_handler(commands=['start'])
async def handle_start(message: types.Message):
    # Создание и отправка кнопки со ссылкой на гайд
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text=data.btn1, url=data.url_pdf_gide)
    keyboard.add(url_button)
    with open(data.WELCOME_PHOTO_PATH, 'rb') as photo:
        await message.bot.send_photo(message.chat.id, photo, caption=data.WELCOME_MESSAGE, parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)

    # Ожидание 1 минуты
    await asyncio.sleep(60)  # Перед запуском раскомментировать!
    # await asyncio.sleep(30)  # Для теста, 30 секунд. Перед запуском закомментировать!

    # Отправка второго сообщения
    await message.answer(data.AUTO_MESSAGE_1 + data.AUTO_MESSAGE_1_1, disable_web_page_preview=False, parse_mode=types.ParseMode.MARKDOWN)

    # Ожидание 60 минут
    await asyncio.sleep(60 * 60)  # Перед запуском раскомментировать!
    # await asyncio.sleep(30)  # Для теста, 30 секунд. Перед запуском закомментировать!

    # Создание и отправка кнопок с вопросами
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text='1', callback_data='question_1')
    button2 = types.InlineKeyboardButton(text='2', callback_data='question_2')
    button3 = types.InlineKeyboardButton(text='3', callback_data='question_3')
    button4 = types.InlineKeyboardButton(text='4', callback_data='question_4')
    keyboard.row(button1, button2)
    keyboard.row(button3, button4)
    await message.answer(data.AUTO_MESSAGE_2 + data.AUTO_MESSAGE_2_2, reply_markup=keyboard, parse_mode="Markdown")

    # Ожидание +6 часов
    await asyncio.sleep(6 * 60 * 60)  # Перед запуском раскомментировать!
    # await asyncio.sleep(30)  # Для теста, 30 секунд. Перед запуском закомментировать!

    # Создание и отправка кнопки со ссылкой на сайт
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text=data.text_url_site, url=data.url_site)
    keyboard.add(url_button)

    with open(data.MESS_3_PHOTO_PATH, 'rb') as photo:
        await message.bot.send_photo(message.chat.id, photo, caption=data.AUTO_MESSAGE_3, parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)

    # Ожидание +6 часов
    await asyncio.sleep(6 * 60 * 60)  # Перед запуском раскомментировать!
    # await asyncio.sleep(30)  # Для теста, 30 секунд. Перед запуском закомментировать!

    # Создание и отправка кнопок для выбора дальнейших действий
    keyboard = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text=data.text_url_telegram, url=data.url_telegram)
    button2 = types.InlineKeyboardButton(text=data.text_url_site_pay, url=data.url_site_pay)
    keyboard.row(button1)
    keyboard.row(button2)

    with open(data.MESS_4_PHOTO_PATH, 'rb') as photo:
        await message.bot.send_photo(message.chat.id, photo, caption=data.AUTO_MESSAGE_4, parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)

# Запуск бота
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(dp.start_polling())
    except KeyboardInterrupt:
        pass
    finally:
        loop.run_until_complete(dp.bot.close())
        loop.close()



# for update:
# import sqlite3
# import data_ignore as data
# import asyncio
# from aiogram import Bot, Dispatcher, types
# from aiogram.contrib.fsm_storage.memory import MemoryStorage
#
# # Подключение к базе данных SQLite
# conn = sqlite3.connect('users.db')
# cursor = conn.cursor()
#
# # Создание таблицы для хранения пользователей
# cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                     id INTEGER PRIMARY KEY,
#                     username TEXT,
#                     user_id INTEGER)''')
# cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_user_id ON users (user_id)")
#
# # Инициализация бота и диспетчера
# bot_token = data.TOKEN
# bot = Bot(token=bot_token)
# storage = MemoryStorage()
# dp = Dispatcher(bot, storage=storage)
#
#
# # Определение функции обратного вызова для обработки нажатий на кнопки с вопросами
# @dp.callback_query_handler(lambda c: c.data.startswith('question_'))
# async def process_question_callback(callback_query: types.CallbackQuery):
#     question_number = callback_query.data.split('_')[1]  # Получение номера вопроса из данных обратного вызова
#
#     # Отправка соответствующего текстового сообщения в зависимости от номера вопроса
#     if question_number == '1':
#         await bot.send_message(callback_query.from_user.id, data.l1, disable_web_page_preview=False)
#     elif question_number == '2':
#         await bot.send_message(callback_query.from_user.id, data.l2, disable_web_page_preview=False)
#     elif question_number == '3':
#         await bot.send_message(callback_query.from_user.id, data.l3, disable_web_page_preview=False)
#     elif question_number == '4':
#         await bot.send_message(callback_query.from_user.id, data.l4, disable_web_page_preview=False)
#
#
# # Обработка команды /start
# @dp.message_handler(commands=['start'])
# async def handle_start(message: types.Message):
#     # Получение информации о пользователе
#     username = '@' + message.from_user.username
#     user_id = message.from_user.id
#
#     # Проверка, существует ли пользователь уже в базе данных
#     cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,))
#     existing_user = cursor.fetchone()
#
#     if existing_user is None:
#         # Сохранение информации о пользователе в базе данных SQLite
#         cursor.execute("INSERT INTO users (username, user_id) VALUES (?, ?)", (username, user_id))
#         conn.commit()
#
#     # Создание и отправка кнопки со ссылкой на гайд
#     keyboard = types.InlineKeyboardMarkup()
#     url_button = types.InlineKeyboardButton(text=data.btn1, url=data.url_pdf_gide)
#     keyboard.add(url_button)
#     with open(data.WELCOME_PHOTO_PATH, 'rb') as photo:
#         await message.bot.send_photo(message.chat.id, photo, caption=data.WELCOME_MESSAGE, parse_mode=types.ParseMode.MARKDOWN, reply_markup=keyboard)
#
#     # Ожидание 1 минуты
#     await asyncio.sleep(60)  # Перед запуском раскомментировать!
#     # await asyncio.sleep(30)  # Для теста, 30 секунд. Перед запуском закомментировать!
#
#     # Отправка второго сообщения
#     await message.answer(data.AUTO_MESSAGE_1 + data.AUTO_MESSAGE_
