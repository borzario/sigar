from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

ib_main = InlineKeyboardButton(text="В начало", callback_data="в начало")
ikb_main = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True).row(ib_main)

b_human = KeyboardButton("Частное лицо")
b_company = KeyboardButton("Компания")
kb_firstwindow = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_firstwindow.add(b_human, b_company)

b_works = KeyboardButton("Услуги компании")
b_adress = KeyboardButton("Адрес компании")
b_call = KeyboardButton("Связаться со специалистом компании")
b_info = KeyboardButton("Справочник")
b_gis = KeyboardButton("Оставить отзыв в 2Гис")
kb_mainwindow = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_mainwindow.row(b_works).row(b_adress).row(b_call).row(b_info).row(b_gis)

b_call_to = KeyboardButton("Заказать звонок")
b_get_contacs = KeyboardButton("Связаться самому")
kb_call = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_call.add(b_call_to, b_get_contacs)

b_user = KeyboardButton("User")
b_admin = KeyboardButton("Admin")
kb_admin_first = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_admin_first.add(b_admin, b_user)

b_dezenfection = KeyboardButton("Дезенфекция")
b_dezinsection = KeyboardButton("Дезинсекция")
b_deratization = KeyboardButton("Дератизация")
b_dezodaration = KeyboardButton("Дезодорация")
kb_servises = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_servises.add(b_dezinsection, b_dezenfection).add(b_deratization, b_dezodaration)

b_coast = KeyboardButton("Расчитать стоимость")
b_master = KeyboardButton("Вызов мастера")
kb_works = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_works.add(b_coast, b_master)

"""Here is admins buttons and keyboards"""
b_get_all_calls = KeyboardButton("Get all calls")
b_get_new_calls = KeyboardButton("Get new calls")
b_close_call = KeyboardButton("Close call")
b_get_all_oders = KeyboardButton("Get all oders")
b_get_new_oders = KeyboardButton("Get new oders")
b_close_oder = KeyboardButton("Close oder")
kb_admin_main = ReplyKeyboardMarkup(resize_keyboard=True)
kb_admin_main.add(b_get_new_calls, b_get_all_calls, b_close_call)
kb_admin_main.row(b_get_new_oders, b_get_all_oders, b_close_oder)

