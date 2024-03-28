import telebot
from telebot import types

bot = telebot.TeleBot('')

@bot.message_handler(commands=['start'])
def start(message):
    first_mess = "Добро пожаловть в парк развлечений Веселая сказка! Желаем Вам приятно провести время!"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    karta = types.KeyboardButton("Карта")
    buy_by_code = types.KeyboardButton("Купить по коду")
    attractions = types.KeyboardButton("Аттракционы")
    markup.add(buy_by_code, attractions, karta)
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "Карта"):
        try:
            bot.send_photo(message.chat.id, 'https://images.app.goo.gl/fJ6v4LubRekAVKBr8');
        except:
            bot.send_message(message.chat.id, "К сожалению, данная функция сейчас не работает.")

    if (message.text == "Купить по коду"):
        bot.send_message(message.chat.id, "Введите код: ", parse_mode='html')

    if (message.text == "Аттракционы"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        kids = types.KeyboardButton("Детская группа")
        family = types.KeyboardButton("Семейная группа")
        extreme = types.KeyboardButton("Экстремальные")
        menu = types.KeyboardButton("В меню")
        markup.add(kids, family, extreme, menu)
        bot.send_message(message.chat.id, text="Выберите тип аттракциона:", reply_markup=markup)

    if (message.text == "Детская группа"):
        print("q")
        #markup = types.InlineKeyboardMarkup(row_width=1)
        '''item = types.InlineKeyboardButton("Авиаторы")
        markup.add(item)
        bot.send_message(message.chat.id, "привет", reply_markup=markup)'''


        #вывод списка аттракционов
        '''# Отправляем картинку
        photo = 'https://images.app.goo.gl/wUXcG46hRES2UDH57'
        bot.send_photo(message.chat.id, photo)

        # Отправляем текстовое описание
        description = "Описание товара"
        bot.send_message(message.chat.id, description)

        # Создаем кнопку "Купить"
        keyboard = telebot.types.InlineKeyboardMarkup()
        buy_button = telebot.types.InlineKeyboardButton(text="Купить", callback_data='buy')
        keyboard.add(buy_button)

        # Отправляем кнопку под сообщением
        bot.send_message(message.chat.id, "Выберите действие:", reply_markup=keyboard)'''

    if (message.text == "В меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        karta = types.KeyboardButton("Карта")
        buy_by_code = types.KeyboardButton("Купить по коду")
        attractions = types.KeyboardButton("Аттракционы")
        markup.add(buy_by_code, attractions, karta)
        bot.send_message(message.chat.id, "Вы вернулись в меню", parse_mode='html', reply_markup=markup)

#для обработки нажатий на кнопку в чате
'''@bot.callback_query_handler(func=lambda call: call.data == 'buy')
def handle_buy_callback(call):
    bot.send_message(call.message.chat.id, "Вы нажали кнопку 'Купить'")'''

# RUN
bot.polling(non_stop=True)
