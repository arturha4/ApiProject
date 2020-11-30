import telebot
from telebot import types
from database import create_user,show_users
from vk_api import get_status
import schedule
token = '1260767500:AAFq0jjuZ6isvMj4OPn8yizFRDmR8yG4Glc'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message,
                 "Привет, я бот для учета времени, я помогу тебе отслеживать твою активность в социальных сетях и не только."
                 " Пока что я работаю только с вк,  введи свой id vk или ник, который находится в адресной строке")
    bot.register_next_step_handler(message,url)


@bot.message_handler(content_types=['text'])
def url(message):
    id=message.text
    markup = types.InlineKeyboardMarkup()
    btn_vk_page= types.InlineKeyboardButton(text='Перейти', url=f'https://vk.com/{id}')
    btn_yes=types.InlineKeyboardButton(text='Да',callback_data='Yes')
    btn_no=types.InlineKeyboardButton(text='Нет',callback_data='No')
    markup.add(btn_vk_page,btn_yes,btn_no)
    bot.send_message(message.chat.id, f"Твоя страница?https://vk.com/{id} ", reply_markup = markup)


@bot.callback_query_handler(func=lambda call:True)
def callback_vk_verify(call):
    try:
        if call.data=='Yes':
            bot.send_message(call.message.chat.id,'Отлично!')
            create_user(call.message.chat.id,call.message.text[call.message.text.find('com/')+4:])
            show_users()
        elif call.data=='No':
            bot.send_message(call.message.chat.id,'Проверь ник ещё раз, если что-то не так введи данные ещё раз')
        bot.edit_message_text(chat_id=call.message.chat.id,message_id=call.message.message_id,text='Ок!',
                              reply_markup=None)
    except Exception as e:
        print(repr(e))






bot.polling(none_stop=True)


#TODO: нужно  сделать чтобы он какое-то определённое время трекал
#чтобы после нажатия  да, при проверке ссылки на вк,  он больше не мог добавлять пользователя вк
