# import telebot
#
# token = '1260767500:AAFq0jjuZ6isvMj4OPn8yizFRDmR8yG4Glc'
# bot = telebot.TeleBot(token)
# #1. получаем id делаем запрос к вк api, делаем ф-ию, котрая считает время в сети
# #2. бот отправлял ссылку на страницу, чтобы проверить верность введённого id, если все верно, ответ кнопка да или нет
# #3. пробовать получить id не ручным вводом
# @bot.message_handler(commands=['start'])
#
#
#
# def start_message(message):
#     bot.reply_to(message,
#                  "Привет, я бот для учета времени, я помогу тебе отслеживать твою активность в социальных сетях и не только."
#                  " Пока что я работаю только с вк,  введи свой id vk или ник, который находится в адресной строке")
#
#
# @bot.message_handler(func=lambda message: True)
# def get_id_vk(message):
#     print(message.text)
#
#
# bot.polling(none_stop=True)
