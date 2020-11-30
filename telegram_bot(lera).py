import telebot
from telebot import types
from database import create_user,show_users
from vk_api import get_status
import schedule

bot = telebot.TeleBot('1260767500:AAFq0jjuZ6isvMj4OPn8yizFRDmR8yG4Glc')

btn_time = telebot.types.ReplyKeyboardMarkup(True, True)
btn_time.row('0⃣0⃣:0⃣0⃣', '0⃣0⃣:1️⃣5️⃣', '0⃣0⃣:3️⃣0⃣', '0⃣0⃣:4️⃣5️⃣')
btn_time.row('0⃣1️⃣:0⃣0⃣','0⃣1️⃣:1️⃣5️⃣','0⃣1️⃣:3️⃣0⃣','0⃣1️⃣:4️⃣5️⃣')
btn_time.row('0⃣2️⃣:0⃣0⃣', '0⃣2️⃣:1️⃣5️⃣','0⃣2️⃣:3️⃣0⃣','0⃣2️⃣:4️⃣5️⃣')
btn_time.row('0⃣3️⃣:0⃣0⃣', '0⃣3️⃣:1️⃣5️⃣', '0⃣3️⃣:3️⃣0⃣', '0⃣3️⃣:4️⃣5️⃣')
btn_time.row('0⃣4️⃣:0⃣0⃣', '0⃣4️⃣:1️⃣5️⃣', '0⃣4️⃣:3️⃣0⃣','0⃣4️⃣:4️⃣5️⃣')
btn_time.row('0⃣5️⃣:0⃣0⃣', '0⃣5️⃣:1️⃣5️⃣', '0⃣5️⃣:3️⃣0⃣', '0⃣5️⃣:4️⃣5️⃣')
btn_time.row('0⃣6️⃣:0⃣0⃣', '0⃣6️⃣:1️⃣5️⃣', '0⃣6️⃣:3️⃣0⃣', '0⃣6️⃣:4️⃣5️⃣')
btn_time.row('0⃣7⃣:0⃣0⃣', '0⃣7⃣:1️⃣5️⃣', '0⃣7⃣:3️⃣0⃣','0⃣7⃣:4️⃣5️⃣')
btn_time.row('0⃣8⃣:0⃣0⃣', '0⃣8⃣:1️⃣5️⃣', '0⃣8⃣:3️⃣0⃣', '0⃣8⃣:4️⃣5️⃣')
btn_time.row('0⃣9⃣:0⃣0⃣', '0⃣9⃣:1️⃣5️⃣', '0⃣9⃣:3️⃣0⃣', '0⃣9⃣:4️⃣5️⃣')
btn_time.row('1️⃣0⃣:0⃣0⃣', '1️⃣0⃣:1️⃣5️⃣', '1️⃣0⃣:3️⃣0⃣', '1️⃣0⃣:4️⃣5️⃣')
btn_time.row('1️⃣1️⃣:0⃣0⃣','1️⃣1️⃣:1️⃣5️⃣', '1️⃣1️⃣:3️⃣0⃣', '1️⃣1️⃣:4️⃣5️⃣')
btn_time.row('1️⃣2️⃣:0⃣0⃣', '1️⃣2️⃣:1️⃣5️⃣', '1️⃣2️⃣:3️⃣0⃣', '1️⃣2️⃣:4️⃣5️⃣')
btn_time.row('1️⃣3️⃣:0⃣0⃣', '1️⃣3️⃣:1️⃣5️⃣', '1️⃣3️⃣:3️⃣0⃣','1️⃣3️⃣:4️⃣5️⃣')
btn_time.row('1️⃣4️⃣:0⃣0⃣', '1️⃣4️⃣:1️⃣5️⃣', '1️⃣4️⃣:3️⃣0⃣', '1️⃣4️⃣:4️⃣5️⃣')
btn_time.row('1️⃣5️⃣:0⃣0⃣', '1️⃣5️⃣:1️⃣5️⃣', '1️⃣5️⃣:3️⃣0⃣', '1️⃣5️⃣:4️⃣5️⃣')
btn_time.row('1️⃣6️⃣:0⃣0⃣', '1️⃣6️⃣:1️⃣5️⃣', '1️⃣6️⃣:3️⃣0⃣','1️⃣6️⃣:4️⃣5️⃣')
btn_time.row('1️⃣7⃣:0⃣0⃣', '1️⃣7⃣:1️⃣5️⃣', '1️⃣7⃣:3️⃣0⃣', '1️⃣7⃣:4️⃣5️⃣')
btn_time.row('1️⃣8⃣:0⃣0⃣', '1️⃣8⃣:1️⃣5️⃣', '1️⃣8⃣:3️⃣0⃣', '1️⃣8⃣:4️⃣5️⃣')
btn_time.row('1️⃣9⃣:0⃣0⃣', '1️⃣9⃣:1️⃣5️⃣', '1️⃣9⃣:3️⃣0⃣','1️⃣9⃣:4️⃣5️⃣')
btn_time.row('2️⃣0⃣:0⃣0⃣', '2️⃣0⃣:1️⃣5️⃣', '2️⃣0⃣:3️⃣0⃣', '2️⃣0⃣:4️⃣5️⃣')
btn_time.row('2️⃣1️⃣:0⃣0⃣', '2️⃣1️⃣:1️⃣5️⃣', '2️⃣1️⃣:3️⃣0⃣', '2️⃣1️⃣:4️⃣5️⃣')
btn_time.row('2️⃣2️⃣:0⃣0⃣', '2️⃣2️⃣:1️⃣5️⃣', '2️⃣2️⃣:3️⃣0⃣','2️⃣2️⃣:4️⃣5️⃣')
btn_time.row('2️⃣3️⃣:0⃣0⃣', '2️⃣3️⃣:1️⃣5️⃣', '2️⃣3️⃣:3️⃣0⃣', '2️⃣3️⃣:4️⃣5️⃣')


@bot.message_handler(content_types=['text'])
def start_message(message):
    dictText = ['Привет', "привет", 'hi', 'hello', 'Hello']
    if message.text in dictText:
        bot.send_message(message.chat.id,
                         "Привет, я бот для учета времени, я помогу тебе отслеживать твою активность "
                         "в социальных сетях и не только!")
        bot.send_message(message.chat.id, "Чтобы выбрать начало трека, нажми команду /start.")
        bot.send_message(message.chat.id, "Чтобы выбрать конец трека, нажми команду /stop.")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    elif message.text == "/start":
        bot.send_message(message.from_user.id, "Выбери время, с которого нужно начать трек.", reply_markup=btn_time)
        bot.register_next_step_handler(message,end_track)
    elif message.text == "/stop":
        bot.send_message(message.from_user.id, "Выбери время, на котором нужно закончить трек.", reply_markup=btn_time)
        bot.register_next_step_handler(message, services)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")


@bot.message_handler()
def end_track(message):
    bot.send_message(message.chat.id, "Выбери время, на котором нужно закончить трек.",reply_markup=btn_time)
    bot.register_next_step_handler(message,services)



@bot.message_handler()
def services(message):
    keyboard = types.InlineKeyboardMarkup()  # клавиатура
    key_vk = types.InlineKeyboardButton(text='VK', callback_data='VK')  # кнопка "vk"
    keyboard.add(key_vk)
    key_urfu = types.InlineKeyboardButton(text='Personal account UrFU', callback_data='Personal account UrFU')
    keyboard.add(key_urfu)
    key_git = types.InlineKeyboardButton(text='GitHub', callback_data='GitHub')  # кнопка "git"
    keyboard.add(key_git)
    question = 'Теперь выбери сервис для поиска страницы.'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)

    @bot.callback_query_handler(func=lambda call: True)
    def callback_worker(call):
        if call.data == "VK":  # call.data это callback_data, указанная при объявлении кнопки
            bot.send_message(message.from_user.id, "Введи свой id vk или ник.")
            bot.register_next_step_handler(message, url_vk)

        if call.data == "Personal account UrFU":
            bot.send_message(message.from_user.id, "Введи свой логин.")
            bot.register_next_step_handler(message, url_urfu)

        if call.data == "GitHub":
            bot.send_message(message.from_user.id, "Введи свой логин.")
            bot.register_next_step_handler(message, url_git)

        if call.data == 'Yes':
            bot.send_message(call.message.chat.id, 'Отлично!')
            # create_user(call.message.text[call.message.text.find('?')-1:])
        elif call.data == 'No':
            bot.send_message(call.message.chat.id, 'Проверь ник ещё раз, если что-то не так введи данные ещё раз')
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ок!',
                              reply_markup=None)

    @bot.message_handler()
    def url_urfu(message):
        bot.send_message(message.chat.id, 'Введи свой пароль.')

    @bot.message_handler()
    def url_vk(message):
        id = message.text
        markup = types.InlineKeyboardMarkup()
        btn_vk_page = types.InlineKeyboardButton(text='Перейти', url=f'https://vk.com/{id}')
        btn_yes = types.InlineKeyboardButton(text='Да', callback_data='Yes')
        btn_no = types.InlineKeyboardButton(text='Нет', callback_data='No')
        markup.add(btn_vk_page, btn_yes, btn_no)
        bot.send_message(message.chat.id, f"Твоя страница? https://vk.com/{id} ", reply_markup=markup)

    def url_git(message):
        id = message.text
        markup = types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id, 'Введи свой пароль.')


bot.polling(none_stop=True)
