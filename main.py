from telebot import *
from telebot.types import *

TOKEN = "6439630036:AAGeOwvMZXszZ_dvGW9gXjV4Jmw1LOR66Ug"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    first_mess = "Добро пожаловть в парк развлечений Весёлая сказка! " \
                 "Желаем Вам приятно провести время! Выберите желаемое действие:"
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    karta = KeyboardButton("Карта")
    buy_by_code = KeyboardButton("Купить по коду")
    attractions = KeyboardButton("Аттракционы")
    markup.add(buy_by_code, attractions, karta)
    bot.send_message(message.chat.id, first_mess, parse_mode="html", reply_markup=markup)


@bot.message_handler(content_types=["text"])
def func(message):
    if message.text == "Карта":
        try:
            bot.send_photo(message.chat.id, "https://images.app.goo.gl/fJ6v4LubRekAVKBr8")
        except:
            bot.send_message(message.chat.id, "К сожалению, данная функция сейчас не работает.")

    if message.text == "Купить по коду":
        bot.send_message(message.chat.id, "Введите код: ", parse_mode="html")

    if message.text == "Аттракционы":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        kids = KeyboardButton("Детская группа")
        family = KeyboardButton("Семейная группа")
        extreme = KeyboardButton("Экстремальные")
        menu = KeyboardButton("В меню")
        markup.add(kids, family, extreme, menu)
        bot.send_message(message.chat.id, text="Выберите тип аттракциона:", reply_markup=markup)

    if message.text == "Детская группа":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        children_playground = KeyboardButton("Детская площадка")
        octopus = KeyboardButton("Осьминожка")
        air_castle = KeyboardButton("Воздушный замок")
        gopher_show = KeyboardButton("Суслик шоу")
        miracle_bar = KeyboardButton("Диво бар")
        airplane = KeyboardButton("Аэроплан")
        humpty_dumpty = KeyboardButton("Шалтай-болтай")
        children_city = KeyboardButton("Детский городок")
        children_gymnasts = KeyboardButton("Детские гимнасты")
        kidkart = KeyboardButton("Детский картинг")
        zig_zag = KeyboardButton("Зиг-Заг")
        fire_brigade = KeyboardButton("Пожарная команда")
        aviators = KeyboardButton("Авиаторы")
        train_chuhchuh = KeyboardButton("Поезд Чух Чух")
        cars = KeyboardButton("Машинки")
        miracles_on_bends = KeyboardButton("Чудеса на виражах")
        house_of_horrors = KeyboardButton("Дом ужасов")
        adventures = KeyboardButton("Приключения пиратов")
        disco = KeyboardButton("Водное диско")
        cheerful_spring = KeyboardButton("Весёлая пружина")
        info = KeyboardButton("Показать все аттракционы детской группы")
        menu = KeyboardButton("В меню")
        markup.add(children_playground, octopus, air_castle, gopher_show, miracle_bar, airplane,
                   humpty_dumpty, children_city, children_gymnasts, kidkart, zig_zag,
                   fire_brigade, aviators, train_chuhchuh, cars, miracles_on_bends,
                   house_of_horrors, adventures, disco, cheerful_spring, info, menu)
        bot.send_message(message.chat.id, text="Выберите аттракцион:", reply_markup=markup)

    if message.text == "Семейная группа":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        island_of_dragons = KeyboardButton("Остров драконов")
        around_the_world = KeyboardButton("Вокруг света")
        wheel_of_vision = KeyboardButton("Колесо обозрения")
        cool_race = KeyboardButton("Крутые гонки")
        catamarans = KeyboardButton("Катамараны")
        big_carousel = KeyboardButton("Большая карусель")
        flamenco = KeyboardButton("Фламенко")
        retro = KeyboardButton("Ретро")
        russian_mountains = KeyboardButton("Русские горки")
        star_patrol = KeyboardButton("Звёздный патруль")
        flying_saucer = KeyboardButton("Летающая тарелка")
        info = KeyboardButton("Показать все аттракционы семейной группы")
        menu = KeyboardButton("В меню")
        markup.add(island_of_dragons, around_the_world, wheel_of_vision, cool_race, catamarans, big_carousel,
                   flamenco, retro, russian_mountains, star_patrol, flying_saucer, info, menu)
        bot.send_message(message.chat.id, text="Выберите аттракцион:", reply_markup=markup)

    if message.text == "Экстремальные":
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        slaughterhouse = KeyboardButton("Великолукский мясокомбинат")
        slaughterhouse2 = KeyboardButton("Великолукский мясокомбинат-2")
        shaker = KeyboardButton("Шейкер")
        hopple = KeyboardButton("Хоппла")
        seven_heaven = KeyboardButton("Седьмое небо")
        free_fall = KeyboardButton("Свободное падение")
        rocket = KeyboardButton("Ракета")
        fifth_element = KeyboardButton("5 элемент")
        big_russian_mountain = KeyboardButton("Большая русская горка")
        winged_swing = KeyboardButton("Крылатые качели")
        catapult = KeyboardButton("Катапульта")
        storm = KeyboardButton("Шторм")
        booster = KeyboardButton("Бустер")
        info = KeyboardButton("Показать все экстремальные аттракционы")
        menu = KeyboardButton("В меню")
        markup.add(slaughterhouse, slaughterhouse2, shaker, hopple, seven_heaven, free_fall, rocket, fifth_element,
                   big_russian_mountain, winged_swing, catapult, storm, booster, info, menu)
        bot.send_message(message.chat.id, text="Выберите аттракцион:", reply_markup=markup)

        # markup = types.InlineKeyboardMarkup(row_width=1)
        '''item = types.InlineKeyboardButton("Авиаторы")
        markup.add(item)
        bot.send_message(message.chat.id, "привет", reply_markup=markup)'''

        # Вывод списка аттракционов
        '''# Отправляем картинку
        photo = "https://images.app.goo.gl/wUXcG46hRES2UDH57"
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

    if message.text == "В меню":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        karta = types.KeyboardButton("Карта")
        buy_by_code = types.KeyboardButton("Купить по коду")
        attractions = types.KeyboardButton("Аттракционы")
        markup.add(buy_by_code, attractions, karta)
        bot.send_message(message.chat.id, "Вы вернулись в меню", parse_mode='html', reply_markup=markup)

    # Детская группа
    if message.text == "Показать все аттракционы детской группы":
        # Вывод перечня аттракционов в чат
        children_playground_info(message)
        octopus_info(message)
        air_castle_info(message)
        gopher_show_info(message)
        miracle_bar_info(message)
        airplane_info(message)
        humpty_dumpty_info(message)
        children_city_info(message)
        children_gymnasts_info(message)
        kid_kart_info(message)
        zig_zag_info(message)
        fire_brigade_info(message)
        aviators_info(message)
        chuh_chuh_info(message)
        cars_info(message)
        miracles_on_bends_info(message)
        house_of_horrors_info(message)
        adventures_info(message)
        disco_info(message)
        cheerful_spring_info(message)

    if message.text == "Детская площадка":
        children_playground_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Осьминожка":
        octopus_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Воздушный замок":
        air_castle_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Суслик шоу":
        gopher_show_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Диво бар":
        miracle_bar_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Аэроплан":
        airplane_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Шалтай-болтай":
        humpty_dumpty_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Детский городок":
        children_city_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Детские гимнасты":
        children_gymnasts_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Детский картинг":
        kid_kart_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Зиг-Заг":
        zig_zag_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Пожарная команда":
        fire_brigade_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Авиаторы":
        aviators_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Поезд Чух Чух":
        chuh_chuh_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Машинки":
        cars_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Чудеса на виражах":
        miracles_on_bends_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Дом ужасов":
        house_of_horrors_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Приключения пиратов":
        adventures_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Водное диско":
        disco_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Весёлая пружина":
        cheerful_spring_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    # Семейная группа
    if message.text == "Показать все аттракционы семейной группы":
        island_of_dragons_info(message)
        around_the_world_info(message)
        wheel_of_vision_info(message)
        cool_race_info(message)
        catamarans_info(message)
        big_carousel_info(message)
        flamenco_info(message)
        retro_info(message)
        russian_mountains_info(message)
        star_patrol_info(message)
        flying_saucer_info(message)

    if message.text == "Остров драконов":
        island_of_dragons_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Вокруг света":
        around_the_world_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Колесо обозрения":
        wheel_of_vision_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Крутые гонки":
        cool_race_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Катамараны":
        catamarans_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Большая карусель":
        big_carousel_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Фламенко":
        flamenco_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Ретро":
        retro_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Русские горки":
        russian_mountains_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Звёздный патруль":
        star_patrol_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Летающая тарелка":
        flying_saucer_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    # Экстремальные
    if message.text == "Великолукский мясокомбинат":
        slaughterhouse_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Великолукский мясокомбинат-2":
        slaughterhouse2_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Шейкер":
        shaker_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Хоппла":
        hopple_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Седьмое небо":
        seven_heaven_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Свободное падение":
        free_fall_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Ракета":
        rocket_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "5 элемент":
        fifth_element_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Большая русская горка":
        big_russian_mountain_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Крылатые качели":
        winged_swing_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Катапульта":
        catapult_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Шторм":
        storm_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Бустер":
        booster_info(message)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buybil = types.KeyboardButton("Купить билет")
        back = types.KeyboardButton("Назад")
        menu = types.KeyboardButton("В меню")
        markup.add(buybil, back, menu)
        bot.send_message(message.chat.id, text="Выберите Действия:", reply_markup=markup)

    if message.text == "Показать все экстремальные аттракционы":
        slaughterhouse_info(message)
        slaughterhouse2_info(message)
        shaker_info(message)
        hopple_info(message)
        seven_heaven_info(message)
        free_fall_info(message)
        rocket_info(message)
        fifth_element_info(message)
        big_russian_mountain_info(message)
        winged_swing_info(message)
        catapult_info(message)
        storm_info(message)
        booster_info(message)

'''def on_click(message):
    # if message.text == "Покупка билета":

    if message.text == "Назад":
        bot.send_message(message.chat.id, "Экстремальные", parse_mode="Markdown")
        #bot.delete_message(message.chat.id)'''
def children_playground_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_1002_0.jpeg?itok=KwRp2JRf"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_1004.jpeg?itok=rXYzT8yp"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_0965_0.jpeg?itok=M6zL_VDU"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/1_0_0.png?itok=LV707-Hz"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Детская площадка*\n\nНастоящая Страна Детства, " \
                  "где можно весело провести время со своими друзьями и, " \
                  "конечно же, приобрести новых. Разнообразные горки, качели, " \
                  "канаты – сложно придумать более насыщенное времяпрепровождение для Вашего маленького непоседы.\n\n" \
                  "*Ограничения:* отсутствуют.\n\n" \
                  "*Цена:* бесплатно."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")
    '''back_button = types.KeyboardButton("Назад")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(back_button)
    bot.register_next_step_handler(message.chat.id, on_click)'''




def octopus_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/2016-06-14-16-10-12.png?itok=xXYc3ALR"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/02.png?itok=dva0P5l9"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/00.png?itok=2gL5VUsp"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/01.png?itok=H4T7V_iF"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Осьминожка*\n\nОгромный, но очень милый осьминог приглашает " \
                  "отважных мореплавателей принять участие в захватывающем " \
                  "морском приключении. Удобно разместившись прямо на его " \
                  "щупальцах, малыши и их родители заскользят по невидимым " \
                  "волнам бескрайнего моря. Брызги восторга захлестнут смельчаков, " \
                  "дерзнувших покорить водную стихию верхом на морском гиганте.\n\n" \
                  "*Ограничения:* для посетителей от 1,2 м.; (дети от 1,05 м. до 1,2 м. " \
                  "в сопровождении взрослого с билетом)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def air_castle_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/00_0.png?itok=WWs6P6yA"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/02_0.png?itok=FNqDdcBf"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/01_0.png?itok=mSPDhTcd"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Воздушный замок*\n\nЧудо всегда возможно в нашем парке. " \
                  "Полет вокруг средневекового замка на чудесных ярких " \
                  "бипланах украсит Ваш день и наполнит его тем самым волшебным " \
                  "настроением, что рождается лишь в детстве, когда по-настоящему веришь " \
                  "в то, что стать героем любимой сказки вполне реально.\n\n" \
                  "*Ограничения:* для посетителей от 1,2 м.; (дети от 0,9 м. до 1,2 м. " \
                  "в сопровождении взрослого с билетом)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def gopher_show_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_0835_2.jpeg?itok=a_rqhia1"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0715_0.jpeg?itok=wopZc6yX"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0806_0.jpeg?itok=uKN9f7c9"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0196.jpg?itok=7SjHhT-2"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Суслик-шоу*\n\n" \
                  "Что может быть увлекательнее, чем совместная игра? " \
                  "Предлагаем Вам всей семьей открыть сезон охоты на уморительных сусликов, " \
                  "настойчиво выпрыгивающих из своих норок. Вам нужно стать еще более стремительным и " \
                  "ловким, чтобы преградить им путь специальным орудием. Захватывающее развлечение " \
                  "для больших и маленьких поднимет командный дух и вдохнет еще больше веселья в " \
                  "Ваше семейное времяпрепровождение.\n\n" \
                  "*Ограничения:* без ограничений\n\n" \
                  "*Цена:* 100 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def miracle_bar_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0675_0.jpeg?itok=HE1tRZZh"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0672.jpeg?itok=x_RGkLSQ"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0367.jpeg?itok=XAn0SmIz"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Диво-бар*\n\nЗамечательный аттракцион для семейных соревнований. " \
                  "С помощью джойстика следует продемонстрировать свою ловкость " \
                  "и умудриться первым наполнить кружку. Кто же окажется победителем? " \
                  "На самом деле, это не так уж важно, потому что азарт охватит всех " \
                  "от мала до велика, а дух соревнования принесет удовольствие " \
                  "не только победителям\n\n" \
                  "*Ограничения:* без ограничений\n\n" \
                  "*Цена:* 100 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def airplane_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8392.jpeg?itok=typqqjqA"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8331_0.jpeg?itok=YXYXIUk-"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8327.jpeg?itok=hU0ScYAb"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Аэроплан*\n\nДетский аттракцион «Аэроплан» осуществит мечту " \
                  "Вашего ребенка почувствовать себя настоящим пилотом. " \
                  "Увлекательный полет на красочном аэроплане ждет маленького " \
                  "смельчака на высоте 8 метров от земли.\n\n" \
                  "*Ограничения:* для посетителей от 0,9 м. до 1,5 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def humpty_dumpty_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8235_1.jpeg?itok=9LiWse0l"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8182_1_0.jpeg?itok=5ewF81xt"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8257_1.jpeg?itok=mq9GSdYa"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Шалтай-болтай*\n\nНаш веселый домик «Шалтай-Болтай» " \
                  "танцует вместе со своими гостями, раскачиваясь из стороны в сторону, " \
                  "вверх и вниз. Маленькие посетители и их родители получат море ярких " \
                  "положительных эмоций, находясь внутри этого красочного чуда.\n\n" \
                  "*Ограничения:* для посетителей от 1,05 м.; (дети от 0,9 м. до 1,05 м. " \
                  "в сопровождении взрослого с билетом)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def children_city_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/d86a9321.jpg?itok=prQrPuBH"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/2_15.png?itok=3TV_i-12"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_0945.jpeg?itok=5UVnNu53"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Детский городок*\n\nНа детской площадке нашего парка расположился " \
                  "городок с множеством занимательных лазеек, качелей и горок для " \
                  "маленьких любителей активного отдыха. Здесь каждый маленький " \
                  "Индиана Джонс найдет себе приключение по душе, наполняя свой " \
                  "день тысячами ярких впечатлений.\n\n" \
                  "*Ограничения:* дети ростом от 0,8 м. до 1,4 м. допускаются на " \
                  "аттракцион только в сопровождении, сопровождающее лицо " \
                  "допускается на аттракцион бесплатно.\n\n" \
                  "*Цена:* бесплатно."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def children_gymnasts_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/3_2.png?itok=0axvSK3W"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_7142.jpeg?itok=db8jZ8fc"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_7112.jpeg?itok=vFgp2Hws"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Детские гимнасты*\n\nЗавораживающие трюки воздушных гимнастов под " \
                  "куполом цирка рождают в детской душе новую мечту, которая в " \
                  "нашем парке становится реальностью. Батут и динамические тросы " \
                  "позволят детям почувствовать себя настоящими звездами цирковой арены.\n\n" \
                  "*Ограничения:* для посетителей до 30 кг.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def kid_kart_info(message):
    # Отправляем картинку (и)
    photo1 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/karting.png?itok=jw_L6U-o"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/karting-1.png?itok=60mGwNy1"
    bot.send_photo(message.chat.id, photo1)
    bot.send_photo(message.chat.id, photo2)
    # Отправляем текстовое описание
    description = "*Детский картинг* \n\nСтать полноправным участником дорожного движения теперь может каждый малыш. " \
                  "Яркие машинки оснащены аккумуляторами и управление ими легко дается даже самым маленьким. " \
                  "Карты передвигаются по правилам, что поможет вашему ребенку подготовиться к изучению " \
                  "правил дорожного движения и научиться дисциплине на дороге.\n\n" \
                  "*Ограничения:* ля посетителей от 1,1 м.; (дети от 0,9 м. до 1,1 м. " \
                  "в сопровождении взрослого без билета). Цена указана за машинку. \n\n" \
                  "*Цена:* 350 руб"
    '''keyboard = telebot.types.InlineKeyboardMarkup()
    buy_button_kidkart = telebot.types.InlineKeyboardButton(text="Купить", callback_data="buy")
    keyboard.add(buy_button_kidkart)
    bot.send_message(message.chat.id, description, parse_mode="Markdown", reply_markup=keyboard)'''
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def zig_zag_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/1_3.png?itok=mNf-VvgZ"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_06791.png?itok=p945SXuj"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_6368.png?itok=G-hlKiRB"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Зиг-Заг*\n\nАттракцион, названный в честь знаменитого диснеевского " \
                  "персонажа Зигзага Маккряка, поднимет маленьких пилотов на высоту " \
                  "5 метров и, сделав несколько виражей, плавно приземлит, наполнив " \
                  "их восторгом настоящего полета. Красочные винтовые самолеты " \
                  "позволят малышам почувствовать себя героями всеми любимого мультфильма.\n\n" \
                  "*Ограничения:* для посетителей от 0,8 м. до 1,3 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def fire_brigade_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc9465_1.jpeg?itok=og8Bp1Yr"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc9472_1.jpeg?itok=OquLNYPc"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc9461_1_0.jpeg?itok=uALU3mPN"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_8386.jpg?itok=zBUn_dTU"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Пожарная команда*\n\nВеселое соревнование ждет юных пожарников на этом " \
                  "увлекательном аттракционе. Из водных пистолетов, как из брандспойта, " \
                  "команда маленьких смельчаков потушит горящий дом. Но кто из них первым " \
                  "справится с задачей? Сила командного духа и незабываемые впечатления " \
                  "гарантированы тем, кто отважится на сражение со стихией.\n\n" \
                  "*Ограничения:* для посетителей от 0,9 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def aviators_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8328.jpeg?itok=78ujkOWL"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8291.jpeg?itok=TFkIdGjN"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8268.jpeg?itok=Ffb_oYYK"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/2.png?itok=QgPfuxcF"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    description = "*Авиаторы* \n\nАттракцион для будущих отважных летчиков носит название «Авиаторы». " \
                  "Красочные самолетики поднимут в своих кабинах малышей и их родителей прямо в небо, " \
                  "подарив ощущение полета и прекрасное настроение тем и другим.\n\n" \
                  "*Ограничения:* для посетителей от 1,05 м.; (дети до 1,05 м. в сопровождении взрослого с билетом)" \
                  "\n\n*Цена:* 250 руб"
    # Убрана кнопка под текстом
    '''keyboard = telebot.types.InlineKeyboardMarkup()
    buy_button_avia = telebot.types.InlineKeyboardButton(text="Купить", callback_data='buy')
    keyboard.add(buy_button_avia)
    bot.send_message(message.chat.id, description, parse_mode="Markdown", reply_markup=keyboard)'''
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def chuh_chuh_info(message):
    # Отправляем картинку (и)
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_5716.jpeg?itok=NLoouWgN"
    bot.send_photo(message.chat.id, photo2)
    # Отправляем текстовое описание
    description2 = "*Поезд Чух Чух*\n\n" \
                   "Захватывающее дух путешествие по Сказочной Долине в паровозике «Чух-чух» покажет малышам мир, " \
                   "в котором царит волшебство. Гигантские ушастые кролики пасутся на поляне, усыпанной " \
                   "редкой красоты тюльпанами, пощипывают травку умилительные ослики, а кто это там прячется " \
                   "в кустах?... Да это же бегемот!\n\n" \
                   "*Ограничения:* От 0,9 м. до 1,3 м. в сопровождении взрослого с билетом и от 1,3м самостоятельно" \
                   "\n\n*Цена:* 250 руб"
    '''keyboard = telebot.types.InlineKeyboardMarkup()
    buy_button_chuhchuh = telebot.types.InlineKeyboardButton(text="Купить", callback_data='buy')
    keyboard.add(buy_button_chuhchuh)
    bot.send_message(message.chat.id, description2, parse_mode="Markdown", reply_markup=keyboard)'''
    bot.send_message(message.chat.id, description2, parse_mode="Markdown")


def cars_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/1-1014.png?itok=tAAVcRIS"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0165.jpg?itok=gi595zB5"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/1-1029.jpg?itok=iPK28-wE"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Машинки*\n\nАттракцион дарит малышам возможность попробовать себя в необычной роли " \
                  "и получить новые яркие впечатления. Красочные яркие автомобильчики ждут маленьких гонщиков, " \
                  "чтобы прокатить их по трассе и дать им почувствовать себя участником легендарной «Формулы-1».\n\n" \
                  "*Ограничения:* для посетителей от 0,9 м. до 1,35 м. (цена за машинку)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def miracles_on_bends_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_5968.png?itok=4j2kwTZS"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_1432_1_0_0.jpg?itok=xGe2_DP-"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/3.jpg?itok=najRoIbh"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    description = "*Чудеса на виражах*\n\nМаленькие экстремалы несомненно получат свою порцию " \
                  "адреналина на аттракционе «Чудеса на виражах». Красочные вагончики бегут по " \
                  "извилистой трассе, унося своих пассажиров в страну неизведанных впечатлений. " \
                  "Русские горки в миниатюре с крутыми виражами, подъемами и спусками " \
                  "подарят море восторга и океан позитивной энергии вашим малышам.\n\n" \
                  "*Ограничения:* для посетителей от 0,9 м. до 1,3 м.\n\n" \
                  "*Цена:* 250 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def house_of_horrors_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/2_4.png?itok=Ph1CT5YA"
    bot.send_photo(message.chat.id, photo)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Тир 'Дом Ужасов'*\n\nВойдите в таинственный дом, где лишь скудные блики света послужат " \
                  "Вам ориентиром в войне с Сумеречным миром. Внезапно отделяющиеся от стен тени, призраки, " \
                  "материализующиеся так внезапно, что кровь леденеет и мурашки предательски ползут по коже. " \
                  "Разного рода нечисть выползает на встречу охотнику, отважно вступившему на путь Света. " \
                  "Но рука его не дрогнет и поразит врага. А самого меткого смельчака ждет ценный трофей!\n\n" \
                  "*Ограничения:* без ограничений\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def adventures_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/2_9.png?itok=avaBDoWm"
    bot.send_photo(message.chat.id, photo)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Тир 'Приключения пиратов'*\n\nИстории о пиратах – это всегда вереница захватывающих " \
                  "приключений, множество опасностей и, конечно, несметные сокровища. Стать пиратом хотя " \
                  "бы на один день мечтает каждый мальчишка – да и девчонка, на самом деле, тоже! Диво " \
                  "Остров приглашает юных пиратов проверить свои силы – храбрость, меткость и настойчивость " \
                  "помогут им завоевать настоящие сокровища в нашем тире «Приключения пиратов».\n\n" \
                  "Благородным юным пиратам предстоит победить страшных морских чудовищ и коварных недругов. " \
                  "Их союзники – верный глаз и твердая рука. И, конечно, мама с папой, которые никогда не " \
                  "дадут в обиду начинающего морского разбойника.Для получения приза («сундук сокровищ») в " \
                  "Тире необходимо набрать:\n\nДля посетителей до 14 лет – 2500 очков\nДля посетителей старше 14 " \
                  "лет – 3500 очков\n\n" \
                  "*Ограничения:* без ограничений\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def disco_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/2_2.png?itok=A_k1Z0V7"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_6824_1.jpeg?itok=cctyv_Ls"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_1116.jpeg?itok=9edEkhgc"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Водное диско*\n\nВсе знают, что можно танцевать на траве, на паркете, даже на льду " \
                  "– а мы предлагаем Вам станцевать на воде! Для этого достаточно освоить навыки управления " \
                  "небольшим, но очень забавным устройством – это маленькая лодочка на резиновой подушке. " \
                  "Она отличается от обычной лодки удивительной способностью «танцевать» по поверхности " \
                  "воды. Механизм управления настолько прост, что с ним справится даже ребенок. А вот " \
                  "кому понравится больше – детям или родителям – судить не нам! Веселое водное диско не " \
                  "оставляет равнодушными никого.\n\n" \
                  "*Ограничения:* для посетителей от 0,9 м. до 1,1 м. в сопровождении взрослого. От 1,1 м." \
                  "самостоятельно (цена за машинку).\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def cheerful_spring_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_6169_1.png?itok=ktofQPQD"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_6276_1.png?itok=uMRhAmZu"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_6845.jpeg?itok=EmlyCiHx"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Весёлая пружина*\n\nВсем детям хочется попробовать что-нибудь взрослое и аттракционы, " \
                  "конечно, не являются исключением. В парке «Диво Остров» вы сможете порадовать своих " \
                  "детей действительно необычайными впечатлениями. Маленькая копия аттракциона «Свободное падение» " \
                  "высотой всего в 15 метров ждет маленьких смельчаков. Медленный подъем и быстрый спуск.\n\n" \
                  "*Ограничения:* для посетителей от 1,1 м.;(дети от 0,9 м. до 1,1 м. в сопровождении " \
                  "взрослого с билетом)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


# Семейная группа
def island_of_dragons_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/2_1.jpeg?itok=zcXzcbDY"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/3_0.jpeg?itok=GKoIaogr"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/4.jpeg?itok=vZtomTQ5"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/5_0.jpg?itok=n4HYW6LR"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Остров драконов* \n\n" \
                  "Насладитесь обзорной экскурсией по Диво острову на высоте 4 метра, путешествуя в мобиле, " \
                  "стилизованном под огромного дракона. Это отличная возможность перевести " \
                  "дух после экстремальных аттракционов и открыть для себя неизведанные уголки нашего парка.\n\n" \
                  "*Ограничения:* самостоятельно от 1,3 м. дети от 0,9 м. до 1,3 м. " \
                  "в сопровождении взрослого за гандолу 4 места.\n\n " \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def around_the_world_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/vokrugsveta4.jpg?itok=bYxSgArz"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/vokrugsveta3.jpg?itok=Ykd2S4bf"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/vokrug-svet.png?itok=lt-O9zvJ"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Вокруг света (за машинку 3 места)*\n\nНасладитесь роскошными видами парка с высоты 4-х метров, " \
                  "путешествуя в мобиле, стилизованном в духе изобретений великого Леонардо. " \
                  "На протяжении пути вы сможете перевести дух после экстремальных аттракционов, " \
                  "полюбоваться окрестностями и наметить дальнейший план получения положительных эмоций. " \
                  "Регулировать скорость передвижения можно с помощью педалей, которыми оснащен каждый мобиль.\n\n" \
                  "*Ограничения:* для посетителей от 1,2 м.;(дети от 0,9 м. до 1,2 м. сопровождающий платно)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def wheel_of_vision_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_9240_1.jpeg?itok=Kwaqh7gw"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_9150_1.jpeg?itok=HZi-xvix"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    # Отправляем текстовое описание
    description = "*Колесо обозрения*\n\nНа Колесе Обозрения Санкт-Петербург, за красоту свою воспетый " \
                  "поэтами и художниками всего мира, явит свое величие с высоты птичьего полета. " \
                  "Один из самых романтичных аттракционов, придуманных нашей цивилизацией, " \
                  "откроет перед Вами перспективу улиц и парков, искрящуюся воду каналов и " \
                  "безупречную архитектуру старого центра. Грандиозная панорама великого города очарует " \
                  "ваш взор и покорит Ваше сердце. Комфортные кабины неспешно движутся по кругу, " \
                  "позволяя Вам и Вашим спутникам сполна насладиться видом одного из " \
                  "самых прекрасных городов мира.\n\n" \
                  "*Ограничения:* для посетителей от 1,1 м.;" \
                  "(дети до 1,1 м. в сопровождении взрослого с билетом)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def cool_race_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/9.jpeg?itok=vHFg_DJp"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8457_1.jpeg?itok=dcNQoeR0"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8449_1.jpeg?itok=71ENp6xS"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    description = "*Крутые гонки*\n\nВы просто не можете упустить возможность лихо погонять на ярких автомобилях! " \
                  "Элементарное управление, крики восторга и веселый смех – три кита, " \
                  "которые доставят Вас и ваших близких в страну беззаботной радости и вечного праздника! " \
                  "За руль может сеть каждый в независимости от возраста и стажа вождения. " \
                  "Крутые гонки – великолепный шанс подрифтовать, не опасаясь последствий.\n\n" \
                  "*Ограничения:* для посетителей от 1,1 м.;" \
                  "(дети до 1,1 м. в сопровождении взрослого с билетом)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def catamarans_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8640.jpeg?itok=Bo682Z_9"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8604.jpeg?itok=NWFMU66j"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Катамараны*\n\nСнискавшие заслуженную популярность неспешные прогулки по " \
                  "водной глади озера на комфортных катамаранах, приобрели в нашем парке " \
                  "новое прочтение. Теперь вы сможете развернуть настоящую водную баталию. " \
                  "Мы предлагаем Вам всей семьей устроить водную перестрелку. " \
                  "Для этой цели мы оснастили катамараны специальными устройствами, " \
                  "которые превратят размеренный променад в настоящее водное сафари. " \
                  "Впрочем, можно обойтись и без стрельбы, ведь романтические прогулки тоже никто не отменял...\n\n" \
                  "*Ограничения:* Дети до 14 лет допускаются на аттракцион в сопровождении взрослых. " \
                  "При катании взимается залог 1 000 руб наличными, " \
                  "который возвращается сразу после посещения аттракциона, " \
                  "квитанцию о залоге нужно сохранять до конца катания, " \
                  "за утерю квитанции накладывается штраф 500 руб.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def big_carousel_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_1209.jpeg?itok=R6wlCX4V"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0134_2.jpeg?itok=366bOQtu"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    # Отправляем текстовое описание
    description = "*Большая карусель*\n\nЭто один из самых красивых аттракционов парка. Башня и барабан " \
                  "«Большой карусели» украшены красочными картинками и разноцветной подсветкой, что, " \
                  "безусловно, привлекает маленьких гостей парка.\n\nКарусель движется очень плавно: " \
                  "сиденья с пассажирами неторопливо поднимаются в воздух, " \
                  "барабан слегка наклоняется и набирает скорость – возникает впечатление, будто " \
                  "Вы кружитесь на мягком облаке, и солнце освещает Вам путь. Восторженные улыбки и " \
                  "детский смех всегда сопровождают катание на Большой Карусели. Приятного полета и Вам!\n\n" \
                  "*Ограничения:* для посетителей от 1,2 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def flamenco_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/qq3e0741.png?itok=5H5dh_6r"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0161.jpeg?itok=kw6SP0sn"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/flamenko2.jpeg?itok=0CCDlTuc"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Фламенко*\n\nТрадиционные ритмы испанского фламенко в мексиканском " \
                  "исполнении – и каждому понятно, что скучать не придется. " \
                  "Новая красочная карусель производит впечатление благодаря непривычной форме. " \
                  "Вместо машинок, лодочек и лошадок мы приглашаем Вас прокатиться в огромных сомбреро.\n\n" \
                  "Кстати: самое большое в мире «настоящее» сомбреро – 4,5 метра в диаметре.\n\n" \
                  "Мы не стремимся побить рекорды: просто наши сомбреро как раз такого размера, " \
                  "чтобы гостям было в них уютно. И – что намного важнее – они танцуют! – " \
                  "веселый мексиканский карнавал под звуки лучших хитов в стиле латино " \
                  "не оставит плохому настроению ни одного шанса.\n\n" \
                  "*Ограничения: *для посетителей от 1,3 м.;(дети от 1,0 м. до 1,3 м. в сопровождении " \
                  "взрослого с билетом)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def retro_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/_dsc8202ob2_1_1_0.png?itok=CXf6B5zZ"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/1_41_1_1.png?itok=hQ0lAngm"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Ретро*\n\nМода на ретро-автомобили не проходит с годами. " \
                  "Они олицетворяют элегантность и роскошь, сдержанность и шик. " \
                  "В то же время ретромобили обладают особым очарованием, " \
                  "словно воссоздавая атмосферу начала XX века.\n\n" \
                  "Наш ретромобиль хорош тем, что он непременно понравится всей семье. " \
                  "Пока взрослые наслаждаются элегантной «винтажной» атмосферой раритетного авто, " \
                  "самые маленькие члены семьи попробуют свои силы за рулем в качестве водителей. " \
                  "Такая семейная прогулка по живописным аллеям парка запомнится надолго – " \
                  "ее тихое очарование часто производит более глубокое впечатление, " \
                  "чем самый экстремальный современный аттракцион. " \
                  "Это маленькое путешествие во времени и – может быть – путешествие к самим себе…\n\n" \
                  "*Ограничения:* от 0,9 до 1,1м в сопровождении взрослого/ от 1,1 м. Самостоятельно.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def russian_mountains_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8603_1_0.jpeg?itok=lDIsRvRN"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8585_1.jpeg?itok=frrHDbJ8"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8578_1.jpeg?itok=2JzV-7Wp"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    description = "*Русские горки*\n\nЭтот аттракцион подойдет тем, кто жаждет экстрима, " \
                  "но предпочитает постепенный накал эмоций и пока не готов покорить саму " \
                  "большую горку парка «Диво Остров». Высота конструкций Русских горок составляет 20 метров, " \
                  "а петли и виражи на 400-метровой трассе заставят ваше сердце биться значительно быстрее, " \
                  "тренируя ваш разум и волю перед подступом к новым вершинам.\n\n" \
                  "*Ограничения:* для посетителей от 1,1 м.\n\n" \
                  "*Цена:* 300 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def star_patrol_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/224_0.jpeg?itok=uaXwIX2O"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/202.jpeg?itok=YrPPKrix"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/199.jpeg?itok=ylkfNJ7b"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Цена выбрана самостоятельно
    # Отправляем текстовое описание
    description = "*Звёздный патруль*\n\nНестареющая история «Звездных войн» снова вернулась в кинотеатры – " \
                  "теперь и в 3D. А у нас, на Диво Острове, загадочный мир Джорджа Лукаса " \
                  "воссоздан в полном цвете и объеме уже давно – пусть и в миниатюре. " \
                  "Любимые персонажи и декорации, знакомые и детям, и взрослым, " \
                  "приходят с экрана в реальный мир!\n\n" \
                  "Поздороваться и сфотографироваться с магистром Йодой, " \
                  "а потом отправиться на борьбу со злом теперь может каждый – " \
                  "возраст не имеет значения. Волшебные приключения и подвиги уже ждут Вас.\n\n" \
                  "*Ограничения:* для посетителей от 1,2 м.;(дети от 0,9 м. до 1,2 м. " \
                  "в сопровождении взрослого с билетом)\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def flying_saucer_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0035.png?itok=tcD_O7zU"
    bot.send_photo(message.chat.id, photo)
    # Цена выбрана самостоятельно
    # Отправляем текстовое описание
    description = "*Летающая тарелка*\n\nДля того, чтобы испытать перегрузки от " \
                  "запуска космического корабля вовсе необязательно вступать в контакт с " \
                  "внеземной цивилизацией или проходить тернистый путь профессионального астронавта. " \
                  "Нарастающая до предельных значений скорость, сопровождаемая " \
                  "соответствующим звуковым рядом, перенесет вас за рамки земных ощущений. " \
                  "Гидравлические цилиндры поднимают конструкцию вверх и она, перетекая из " \
                  "одной плоскости в другую, создает чувство полной космической невесомости.\n\n" \
                  "*Ограничения:* для посетителей от 1,3 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


# Экстремальные
def slaughterhouse_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_5386_1.jpeg?itok=SSk7_zYL"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_1287.jpeg?itok=8KTpPAwq"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_1270.jpeg?itok=ELEDoCBG"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/2015_divoostro_" \
             "velikolukskymiasokombinat_09.jpeg?itok=1jTcSRk7"
    photo5 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_1286.jpeg?itok=SRbQUDJ5"
    photo6 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_1_0.png?itok=fswFA86E"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    bot.send_photo(message.chat.id, photo5)
    bot.send_photo(message.chat.id, photo6)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Великолукский мясокомбинат*\n\n" \
                  "С гордостью представляем вам один из самых масштабных аттракционов в нашей стране. " \
                  "Пневмозапуск с последующим разгоном до 100 км/час за 2 секунды рывком вызволят " \
                  "вас из тесных рамок привычной реальности и переместят в мир иных физических законов. " \
                  "Ваше тело испытает невероятный прилив адреналина, кульминацией которого " \
                  "станет единственная в России петля Иммельмана. Крутые спуски, вращение, " \
                  "свободное падение – за несколько минут вы испытаете весь спектр этих ощущений, " \
                  "в финале трансформирующихся в беспредельный, бьющий через край восторг…\n\n" \
                  "*Ограничения:* для посетителей от 1,3 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def slaughterhouse2_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dkvr_2_0.png?itok=gQS46azS"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/belv0083_2_2.jpg?itok=YbaDzo0d"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/belv0087_2_2.jpg?itok=8fRidzgK"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/belv0097_2_3.jpg?itok=_fAUVel2"
    photo5 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/belv430079_2.jpg?itok=o9TUOHSQ"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    bot.send_photo(message.chat.id, photo5)
    # Отправляем текстовое описание
    description = "*Великолукский мясокомбинат-2*\n\n" \
                  "Хочешь узнать, что значит прыгнуть в бездну с высоты 33 метров и " \
                  "вращаясь в невесомости пролетать над землей? Квинтэссенция чистого адреналина и " \
                  "венец творения инженерной мысли горка «Великолукский мясокомбинат 2» " \
                  "- это невероятные виражи, 10 непрерывных мертвых петель и вертикальный " \
                  "спуск на скорости 90 км/ч. Приходи и проверь на что способен именно ты!\n\n" \
                  "*Ограничения:* для посетителей от 1,4 м. до 1,96 м.\n\n" \
                  "*Цена:* 500 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def shaker_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8477_1_0.jpeg?itok=hxjf1WNh"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8464_1_1.jpeg?itok=75pjTSgY"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8453_0.jpeg?itok=dlVdniWT"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8451_0.jpeg?itok=xi0Ywh-w"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Шейкер*\n\nОригинальный коктейль из ощущений, в котором искусно " \
                  "смешаны скорость, звук и вращение в трех плоскостях. " \
                  "Аттракцион «Шейкер» обладает способностью вытеснять из сознания все лишнее " \
                  "и заполнять его безбрежной радостью, с легкой примесью возбуждения и страха. " \
                  "Мажорные аккорды звукового сопровождения и невообразимые световые эффекты станут " \
                  "той самой вишенкой на торте из впечатлений вашего дня.\n\n" \
                  "*Ограничения:* для посетителей от 1,4 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def hopple_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_6425_1.jpeg?itok=HPdcLRPK"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/d86a2211.jpg?itok=XuYcAYp5"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Хоппла*\n\nНа аттракционе «Хоппла» вы пронесетесь по окружности диаметром " \
                  "в 20 м, совершая полные обороты в 360 градусов. Огромная центрифуга, " \
                  "сочетающая в себе черты «Бустера», «Шейкера» и «Пятого элемента» - " \
                  "это новый способ познать границы своей устойчивости к страху и ощутить, " \
                  "как закипает кровь, заряженная ударной порцией адреналина.\n\n" \
                  "*Ограничения:* для посетителей ростом от 1,32 м. до 1,9 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def seven_heaven_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_5511_4.png?itok=XoLdx2Uv"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_5576.jpeg?itok=UEw5U04x"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0134_4_0.png?itok=FlStAUoq"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Седьмое небо*\n\nВзлететь к небесам и, задыхаясь от восторга, " \
                  "парить, любуясь прекрасным городом с высоты птичьего полета. " \
                  "Мечтали ли вы когда-нибудь об этом? Если – да, то ваша мечта " \
                  "намного ближе к реальности, чем можно было подумать. " \
                  "Садитесь в кресло и откройте глаза навстречу ветру и облакам. " \
                  "Вы подниметесь на высоту 80 метров, а мягкое вращение " \
                  "позволит вам насладиться обзором всей розы ветров.\n\n" \
                  "*Ограничения:* для посетителей от 1,2 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def free_fall_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0217_3_0_1.png?itok=RSdFoWUT"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0217_3_1.png?itok=CmkLWgf4"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/qq3e3212_1_0.png?itok=GP-U4K6p"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Свободное падение*\n\n«Все длиньше и длиньше» - " \
                  "думала Алиса, падая в пропасть» … Сон кэролловской " \
                  "Алисы знаком многим. Ах, если бы можно было испытать " \
                  "такое падение наяву и не разбиться… Смеем вас заверить, " \
                  "даже такая возможность найдет своего искателя в парке " \
                  "«Диво Остров». Вы подниметесь на высоту 60 метров, " \
                  "а потом резко и без предупреждения упадете вниз, " \
                  "вынудив свое ошарашенное сознание устремиться вслед за вами. " \
                  "Сильный положительный стресс и безграничный восторг вам обеспечены.\n\n" \
                  "*Ограничения:* для посетителей от 1,3 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def rocket_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/raketa.jpeg?itok=ZpcuRKAj"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_2924_0.png?itok=QhvrQ94-"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_2835.png?itok=clBv1OLd"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_2846_1_0.png?itok=yk4sNGJ6"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    description = "*Ракета*\n\nКонечно же, мы не могли обойти тему космоса стороной: " \
                  "мы верим, что в каждом из нас жив и ждет своего часа отважный " \
                  "космонавт. И специально для него в нашем парке есть почти " \
                  "настоящая ракета. Разрезав атмосферу на скорости 60 км/час на " \
                  "высоте 50 метров, вы на себе испытаете что такое перегрузка при " \
                  "запуске. Вращение вокруг центральной оси позволит легко представить, " \
                  "что вы вышли на орбиту планеты.\n\n" \
                  "*Ограничения:* для посетителей от 1,25 м. до 1,95 м.\n\n" \
                  "*Цена:* 1000 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def fifth_element_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_2681.png?itok=2O83qiJb"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_2577.png?itok=JCgbGgVj"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_2692.png?itok=I7OO8kHn"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_2590.png?itok=dfBu4auK"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    description = "*5 элемент*\n\nКосмическая одиссея продолжается. Лаконичный диск, " \
                  "отчетливо напоминающий таинственную летающую тарелку, вращаясь во всех " \
                  "плоскостях, на огромной скорости поднимет вас на высоту 35 метров, " \
                  "где меняются местами земля и небо. «Пятый элемент» призван дополнить " \
                  "вашу коллекцию опыта мистическим чувством невесомости.\n\n" \
                  "*Ограничения:* для посетителей от 1,32 м. до 1,9 м.\n\n" \
                  "*Цена:* 400 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def big_russian_mountain_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_7018_1_0.jpeg?itok=Qr_8X-Bu"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8393.jpeg?itok=AUBzrO6v"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/129.jpeg?itok=9eYJobl8"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Большая русская горка*\n\nОгромная скорость, неожиданные маневры, " \
                  "виражи, подъемы, спуски – неотъемлемые атрибуты русских горок " \
                  "еще со времен Петра Великого, по приказу которого были возведены " \
                  "прародители современных – ледяные горки 25 метров высотой. " \
                  "За триста лет полозья сменились колесами, глыбы льда – железными " \
                  "конструкциями, скорость росла, трассы усложнялись и удлинялись. " \
                  "В парке «Диво Остров» вы сможете опробовать венец трехсотлетней " \
                  "истории этого аттракциона и обняться с ветром на высоте более " \
                  "50 метров, летя по трассе длинной в 1,5 км.\n\n" \
                  "*Ограничения:* для посетителей от 1,3 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def winged_swing_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_5380.png?itok=n5DegNeW"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/krylatye-kacheli_2.png?itok=kBW6oHyP"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_5413.jpeg?itok=xS0KSjLR"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Крылатые качели*\n\nКачели – крылья детства, " \
                  "которые живут в душе каждого взрослого. " \
                  "Мы выросли и крылья выросли вместе с нами. " \
                  "Пожалуй, самые впечатляющие качели, из тех, что " \
                  "вы сможете вспомнить, ждут вас в парке «Очень Веселая Сказка». " \
                  "Они вознесут вас на высоту 25 метров и заставят ваше " \
                  "сердце трепетать от страха и восторга, как и тогда, " \
                  "много лет назад.\n\n" \
                  "*Ограничения:* для посетителей от 1,3 м (ниже не допускаем).\n\n" \
                  "*Цена:* 350$."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")
    '''bot.register_next_step_handler(message, on_click)'''





def catapult_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_7601_0.png?itok=BYJlnPKg"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_7560_0.png?itok=IyLju-cF"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc8019_111.jpeg?itok=3APuXLIe"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    # Отправляем текстовое описание
    description = "*Катапульта*\n\nНе всякий рискнет " \
                  "испытать на себе настоящие перегрузки бешеного " \
                  "ускорения. Кто-то вполне удовлетворится рассказами " \
                  "барона Мюнгхаузена о его бесстрашном полете на " \
                  "пушечном ядре и спокойно пойдет пить чай. " \
                  "Но есть и такие, кто примет вызов и взлетит на " \
                  "высоту 80 метров всего за 4 секунды, а после попадет " \
                  "в центрифугу вращения на прямо-таки парализующей " \
                  "волю высоте, испытав ощущения, которые невозможно " \
                  "забыть ни при каких обстоятельствах. А вы, " \
                  "кстати, примите вызов или пойдете пить чай?\n\n" \
                  "*Ограничения:* для посетителей от 1,2 м.\n\n" \
                  "*Цена:* 1000 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def storm_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_6496_1.jpeg?itok=P6JiKccQ"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_6363_1.jpeg?itok=CCVrBh5L"
    photo3 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0149_0.png?itok=HlCx-ab2"
    photo4 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_6579.png?itok=er7o2jq2"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    bot.send_photo(message.chat.id, photo3)
    bot.send_photo(message.chat.id, photo4)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Шторм*\n\nНесложно догадаться, что этот аттракцион " \
                  "несет в себе черты стихии, с которой сражались самые " \
                  "отважные представители человечества во все времена. " \
                  "Гигантская гондола поднимет вас на гребень цунами в " \
                  "30 метров высотой, а Посейдон испытает ваши нервы на " \
                  "крепость, крутя лодку во всех направлениях. " \
                  "Вы узнаете, что такое быть мореплавателем посреди " \
                  "безумной бушующей стихии и почувствуете, как шторм " \
                  "управляет вашим телом и разумом.\n\n" \
                  "*Ограничения:* для посетителей от 1,45 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


def booster_info(message):
    # Отправляем картинку (и)
    photo = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/img_8878.jpeg?itok=3biOdzBo"
    photo2 = "https://www.divo-ostrov.ru/files/styles/attr_gal/public/attraction/dsc_0217_3_0_0.png?itok=EIOgQmEp"
    bot.send_photo(message.chat.id, photo)
    bot.send_photo(message.chat.id, photo2)
    # Отправляем текстовое описание
    # Цена выбрана самостоятельно
    description = "*Бустер*\n\nЛегендарный аттракцион, тот самый, о котором, " \
                  "перефразируя Ларошфуко «все говорят, но мало кто отважился " \
                  "испытать». Огромная конструкция обладает несравненным " \
                  "набором функций, обеспечивающим истинное испытание для инстинкта " \
                  "самосохранения самых искушенных экстремалов. На высоте 50 " \
                  "метров от земли и на скорости вращения 9 оборотов в минуту, " \
                  "вы прочувствуете полную дезориентацию в пространстве и " \
                  "дикий первобытный восторг. А ваши кресла будут предательски " \
                  "раскачиваться, повинуясь силе гравитации и заставляя " \
                  "ваши виски стучать от волн прибывающего адреналина.\n\n" \
                  "*Ограничения:* для посетителей от 1,4 м. до 2,08 м.\n\n" \
                  "*Цена:* 350 руб."
    bot.send_message(message.chat.id, description, parse_mode="Markdown")


# Для обработки нажатий на кнопку в чате
@bot.callback_query_handler(func=lambda call: call.data == "buy")
def handle_buy_callback(call):
    bot.send_message(call.message.chat.id, "Вы нажали кнопку 'Купить'")


# RUN
bot.polling(non_stop=True)
