#t.me/xanax01d

from datetime import datetime, timedelta #для просчета недели (файл week.py)
import gspread #подключаем библиотеку для синхронизации с гугл диском и таблицами
import telebot #подключаем библиотеку для создания ботов 
from telebot import types #импортируем типы для создания клавиатуры в боте
import sqlite3 #подключаем библиотеку для использования баз данных
from week import return_week #используем внешний скрипт для просчета недель
from time import sleep

base = sqlite3.connect('bot_base.db',check_same_thread = False) #подключаем базу
cursor = base.cursor()
bot = telebot.TeleBot('6082835173:AAHhHhrGjGbZoL_PKXNu820m0yQKBNkNtQ0') #токен бота (при создании в @botfather получаем)
gr_list = ['ИТ - 291','СП - 291']
gc = gspread.service_account(filename = 'telegram-383417-054a31246b9f.json') #токен для подключения библиотеки к созданному приложению 
it291_sh = '1jH0cCxM1obOCuA7phpZf1o9IidFpsGLPR3McIgoMoUU' #ключ на расписание ИТ-291
sp291_sh = '1fejVj9VbSRilj6U5sRhxNhf2itkgDtbx0k2xDwp_vqg' #ключ на расписание СП-291
l_d = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']
user_id = 0
user_group = ''
weekn = return_week()
week = ''
data_row = ''
sc = ''
gr = ''

if weekn == 1: 
	week = '1 неделя' #если первая ,открываем лист с названием "1 неделя"
if weekn == 2:
	week = '2 неделя' #если вторая,открываем лист с названием "2 неделя"
if weekn == 3:
	week = '3 неделя' #если третья,открываем лист с названием "3 неделя"
if weekn == 4:
	week = '4 неделя' #если четвертая,открываем лист с названием "4 неделя"

def db_add_user(user_id:int,user_group:str):
	cursor.execute(f"SELECT user_id FROM users_group WHERE user_id = {user_id}")
	data = cursor.fetchone()
	if data is None:
		cursor.execute("INSERT or REPLACE into users_group VALUES (?,?);",(user_id,user_group))
		base.commit()
	else:
		cursor.execute("REPLACE into users_group VALUES(?,?);",(user_id,user_group))
		base.commit()

@bot.message_handler(commands=['start']) #реакция бота на команду /start
def start(message): 
	cursor.execute("""CREATE TABLE IF NOT EXISTS users_group(
		user_id INTEGER PRIMARY KEY NOT NULL,
		user_group TEXT
		)""")
	base.commit()
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	btn1 = types.KeyboardButton("ВО")
	btn2 = types.KeyboardButton("ССО")
	bot.send_message(message.chat.id, text="Добро пожаловать в расписание академии!".format(message.from_user))
	markup.add(btn1,btn2)
	bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
	bot.register_next_step_handler(message,level);
@bot.message_handler(content_types=['text'])
def level(message):
	if (message.text == "ВО"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("1 курс")
		btn2 = types.KeyboardButton("2 курс")
		btn3 = types.KeyboardButton("3 курс")
		btn4 = types.KeyboardButton("4 курс")
		markup.add(btn1,btn2,btn3,btn4)
		bot.send_message(message.chat.id, text="Выберите курс,на котором вы обучаетесь".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,course);
	elif message.text == "ССО":
		bot.send_message(message.chat.id, text="Еще не готово,i'm sorry :(")
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		bot.send_message(message.chat.id, text="Добро пожаловать в расписание академии!".format(message.from_user))
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
	else:
		bot.send_message(message.chat.id,text = "Ты по моему перепутал,возвращаю тебя обратно")
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def course(message):
	if (message.text == "1 курс"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ИТ - 291")
		btn2 = types.KeyboardButton("СП - 291")
		btn3 = types.KeyboardButton("МС - 291")
		btn4 = types.KeyboardButton("ИП - 291")
		btn5 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif message.text == "2 курс":
		bot.send_message(message.chat.id,text = "Еще не готово,i'm sorry :(")
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
	elif message.text == "3 курс":
		bot.send_message(message.chat.id,text = "Еще не готово,i'm sorry :(")
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
	elif message.text == "4 курс":
		bot.send_message(message.chat.id,text = "Еще не готово,i'm sorry :(")
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
	elif message.text == "Назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("1 курс")
		btn2 = types.KeyboardButton("2 курс")
		btn3 = types.KeyboardButton("3 курс")
		btn4 = types.KeyboardButton("4 курс")
		markup.add(btn1,btn2,btn3,btn4)
		bot.send_message(message.chat.id, text="Выберите курс,на котором вы обучаетесь".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,course);
	else:
		bot.send_message(message.chat.id,text = "Еще не готово,i'm sorry :(")
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
@bot.message_handler(content_types=['text'])
def group(message):
	global us_id
	global gr
	if message.text == 'ИТ - 291':
		us_id = message.from_user.id
		gr = "ИТ - 291"
		db_add_user(user_id = us_id,user_group = gr);
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = "Понедельник"
		btn2 = "Вторник"
		btn3 = "Среда"
		btn4 = "Четверг"
		btn5 = "Пятница"
		btn6 = "Суббота"
		btn7 = "Назад"
		markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7)
		bot.send_message(message.chat.id, text="Выберите день".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,day);
	elif message.text == "СП - 291":
		us_id = message.from_user.id
		gr = "СП - 291"
		db_add_user(user_id = us_id,user_group = gr);
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = "Понедельник"
		btn2 = "Вторник"
		btn3 = "Среда"
		btn4 = "Четверг"
		btn5 = "Пятница"
		btn6 = "Суббота"
		btn7 = "Назад"
		markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7)
		bot.send_message(message.chat.id, text="Выберите день".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,day);
	elif message.text == "МС - 291":
		bot.send_message(message.chat.id,text = "Еще не готово,i'm sorry :(")
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ИТ - 291")
		btn2 = types.KeyboardButton("СП - 291")
		btn3 = types.KeyboardButton("МС - 291")
		btn4 = types.KeyboardButton("ИП - 291")
		btn5 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif message.text == "ИП - 291":
		bot.send_message(message.chat.id,text = "Еще не готово,i'm sorry :(")
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ИТ - 291")
		btn2 = types.KeyboardButton("СП - 291")
		btn3 = types.KeyboardButton("МС - 291")
		btn4 = types.KeyboardButton("ИП - 291")
		btn5 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif message.text == "Назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("1 курс")
		btn2 = types.KeyboardButton("2 курс")
		btn3 = types.KeyboardButton("3 курс")
		btn4 = types.KeyboardButton("4 курс")
		markup.add(btn1,btn2,btn3,btn4)
		bot.send_message(message.chat.id, text="Выберите курс,на котором вы обучаетесь".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,course);
	else:
		bot.send_message(message.chat.id,text = "Еще не готово,i'm sorry :(")
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ИТ - 291")
		btn2 = types.KeyboardButton("СП - 291")
		btn3 = types.KeyboardButton("МС - 291")
		btn4 = types.KeyboardButton("ИП - 291")
		btn5 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
@bot.message_handler(content_types=['text'])
def day(message):
	global sh
	global worksheet
	us_id = message.from_user.id
	cursor.execute(f"SELECT user_group FROM users_group WHERE user_id = {us_id}")
	gr:str = ""
	gr_row = cursor.fetchall();
	gr = '' + gr_row[0][0]
	if gr == 'ИТ - 291':
		table = 'schedule_it291'
		cursor.execute(f'SELECT sc FROM {table}')
		schedule = cursor.fetchall()
	elif gr == 'СП - 291':
		table = 'schedule_sp291'
		cursor.execute(f'SELECT sc FROM {table}')
		schedule = cursor.fetchall()
	if message.text == "Понедельник":
		d = schedule[0]
		bot.send_message(message.chat.id,text = d)
		bot.register_next_step_handler(message,day);
	elif message.text == "Вторник":
		d = schedule[1]
		bot.send_message(message.chat.id,text = d)
		bot.register_next_step_handler(message,day);
	elif message.text == "Среда":
		d = schedule[2]
		bot.send_message(message.chat.id,text = d)
		bot.register_next_step_handler(message,day);
	elif message.text == "Четверг":
		d = schedule[3]
		bot.send_message(message.chat.id,text = d)
		bot.register_next_step_handler(message,day);
	elif message.text == "Пятница":
		d = schedule[4]
		bot.send_message(message.chat.id,text = d)
		bot.register_next_step_handler(message,day);
	elif message.text == "Суббота":
		d = schedule[5]
		bot.send_message(message.chat.id,text = d)
		bot.register_next_step_handler(message,day);
	elif message.text == "Назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ИТ - 291")
		btn2 = types.KeyboardButton("СП - 291")
		btn3 = types.KeyboardButton("МС - 291")
		btn4 = types.KeyboardButton("ИП - 291")
		btn5 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
bot.polling(non_stop = True)