from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

ib_main = InlineKeyboardButton(text="В начало", callback_data="в начало")
ikb_main = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).row(ib_main)

b_works = KeyboardButton("Услуги компании")
b_adress = KeyboardButton("Адрес компании")
b_call = KeyboardButton("Связаться со специалистом компании")
b_info = KeyboardButton("Справочник")
b_gis = KeyboardButton("Оставить отзыв в 2Гис")
kb_mainwindow = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_mainwindow.row(b_works).row(b_adress).row(b_call).row(b_info).row(b_gis)


"""
b_time = KeyboardButton("Режим работы")
b_adress = KeyboardButton("Адрес")
b_contacts = KeyboardButton("Контакты")
b_first = KeyboardButton("В начало")
b_usligi = KeyboardButton("Услуги нашего заведения")
b_about = KeyboardButton("О нашем баре")
kb_mainwindow = ReplyKeyboardMarkup(resize_keyboard=True)
kb_mainwindow.row(b_usligi).row(b_about)

b_masters = KeyboardButton("Наши мастера")
b_interier = KeyboardButton("Интерьер")
ib_about = InlineKeyboardButton(text="Назад", callback_data="О нашем баре")
kb_ourbar = ReplyKeyboardMarkup(resize_keyboard=True)
kb_ourbar.row(b_masters).row(b_interier).row(b_time, b_adress, b_contacts)
ikb_main = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).row(ib_main)
ikb_about = InlineKeyboardMarkup(row_width=1).row(ib_about)"""