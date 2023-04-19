#t.me/xanax01d

from datetime import datetime, timedelta
import gspread #подключаем библиотеку для синхронизации с гугл диском и таблицами
import telebot #подключаем библиотеку для создания ботов 
from telebot import types #импортируем типы для создания клавиатуры в боте
import sqlite3
import random
from week import return_week

base = sqlite3.connect('bot_base.db',check_same_thread = False) #подключаем базу
cursor = base.cursor()

bot = telebot.TeleBot('6082835173:AAHhHhrGjGbZoL_PKXNu820m0yQKBNkNtQ0') #токен бота (при создании в @botfather получаем)

gc = gspread.service_account(filename = 'telegram-383417-054a31246b9f.json') #токен для подключения библиотеки к созданному приложению 
it291_sh = '1jH0cCxM1obOCuA7phpZf1o9IidFpsGLPR3McIgoMoUU' #ключ на расписание ИТ-291
sp291_sh = '1fejVj9VbSRilj6U5sRhxNhf2itkgDtbx0k2xDwp_vqg' #ключ на расписание СП-291

user_id = 0
user_group = ''
weekn = return_week();
print(weekn)
week = ''


if weekn == 1: 
	week = '1 неделя' #если первая ,открываем лист с названием "1 неделя"
if weekn == 2:
	week = '2 неделя' #если вторая,открываем лист с названием "2 неделя"
if weekn 	== 3:
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
	if message.text == "ИТ - 291":
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
	print(gr)
	if gr == "СП - 291":
		sh = gc.open_by_key(sp291_sh)
	elif gr == "ИТ - 291":
		sh = gc.open_by_key(it291_sh)
	if message.text == "Понедельник":	
		worksheet = sh.worksheet(f"{week}")
		p11 = worksheet.acell('C3').value
		p12 = worksheet.acell('D3').value
		p21 = worksheet.acell('C4').value
		p22 = worksheet.acell('D4').value
		p31 = worksheet.acell('C5').value
		p32 = worksheet.acell('D5').value
		p41 = worksheet.acell('C6').value
		p42 = worksheet.acell('D6').value
		p51 = worksheet.acell('C7').value
		p52 = worksheet.acell('D7').value
		d = f'Расписание на понедельник'
		s1 = f'1 пара (8:00 - 9:40)'
		s2 = f'2 пара (9:55 - 11:35)'
		s3 = f'3 пара (12:15 - 13:55)'
		s4 = f'4 пара (14:10 - 15:50)'
		s5 = f'5 пара (16:20 - 18:00)'
		o1 = f''
		if p11 == p12:
			if p11 == "!":
				s1 = f'{s1}\nНа расслабоне, на чиле\n'
			else:
				s1 = f'{s1}\n{p11}\n'
		else:
			s1 = f'{s1}\n{p11} | {p12},\n'
		if p21 == p22:
			if p21 == "!":
				s2 = f'{s2}\nНа расслабоне, на чиле\n'
			else:
				s2 = f'{s2}\n{p21}\n'
		else:
			s2 = f'{s2}\n{p21} | {p22}\n'
		if p31 == p32:
			if p31 == "!":
				s3 = f'{s3}\nНа расслабоне, на чиле\n'
			else:
				s3 = f'{s3}\n{p31}\n'
		else:
			s3 = f'{s3}\n{p31} | {p32}\n'
		if p41 == p42:
			if p41 == "!":
				s4 = f'{s4}\nНа расслабоне, на чиле\n'
			else:
				s4 = f'{s4}\n{p41}\n'
		else:
			s4 = f'{s4}\n{p41} | {p42}\n'
		if p51 == p52:
			if p51 == "!":
				s5 = f'{s5}\nНа расслабоне, на чиле\n'
			else:
				s5 = f'{s5}\n{p51}\n'
		else:
			s5 = f'{s5}\n{p51} | {p52}\n'
		o = f'{d}\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}'
		print (o)
		bot.send_message(message.chat.id,text = o)
		bot.register_next_step_handler(message,day);
	elif message.text == "Вторник":	
		worksheet = sh.worksheet(f"{week}")
		p11 = worksheet.acell('C10').value
		p12 = worksheet.acell('D10').value
		p21 = worksheet.acell('C11').value
		p22 = worksheet.acell('D11').value
		p31 = worksheet.acell('C12').value
		p32 = worksheet.acell('D12').value
		p41 = worksheet.acell('C13').value
		p42 = worksheet.acell('D13').value
		p51 = worksheet.acell('C14').value
		p52 = worksheet.acell('D14').value
		d = f'Расписание на Вторник'
		s1 = f'1 пара (8:00 - 9:40)'
		s2 = f'2 пара (9:55 - 11:35)'
		s3 = f'3 пара (12:15 - 13:55)'
		s4 = f'4 пара (14:10 - 15:50)'
		s5 = f'5 пара (16:20 - 18:00)'
		o1 = f''
		if p11 == p12:
			if p11 == "!":
				s1 = f'{s1}\nНа расслабоне, на чиле\n'
			else:
				s1 = f'{s1}\n{p11}\n'
		else:
			s1 = f'{s1}\n{p11} | {p12},\n'
		if p21 == p22:
			if p21 == "!":
				s2 = f'{s2}\nНа расслабоне, на чиле\n'
			else:
				s2 = f'{s2}\n{p21}\n'
		else:
			s2 = f'{s2}\n{p21} | {p22}\n'
		if p31 == p32:
			if p31 == "!":
				s3 = f'{s3}\nНа расслабоне, на чиле\n'
			else:
				s3 = f'{s3}\n{p31}\n'
		else:
			s3 = f'{s3}\n{p31} | {p32}\n'
		if p41 == p42:
			if p41 == "!":
				s4 = f'{s4}\nНа расслабоне, на чиле\n'
			else:
				s4 = f'{s4}\n{p41}\n'
		else:
			s4 = f'{s4}\n{p41} | {p42}\n'
		if p51 == p52:
			if p51 == "!":
				s5 = f'{s5}\nНа расслабоне, на чиле\n'
			else:
				s5 = f'{s5}\n{p51}\n'
		else:
			s5 = f'{s5}\n{p51} | {p52}\n'
		o = f'{d}\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}'
		print (o)
		bot.send_message(message.chat.id,text = o)
		bot.register_next_step_handler(message,day);
	elif message.text == "Среда":
		worksheet = sh.worksheet(f"{week}")
		p11 = f'{worksheet.acell("C17").value}'
		p12 = f'{worksheet.acell("D17").value}'
		p21 = f'{worksheet.acell("C18").value}'
		p22 = f'{worksheet.acell("D18").value}'
		p31 = f'{worksheet.acell("C19").value}'
		p32 = f'{worksheet.acell("D19").value}'
		p41 = f'{worksheet.acell("C20").value}'
		p42 = f'{worksheet.acell("D20").value}'
		p51 = f'{worksheet.acell("C21").value}'
		p52 = f'{worksheet.acell("D21").value}'
		d = f'Расписание на Среду'
		s1 = f'1 пара (8:00 - 9:40)'
		s2 = f'2 пара (9:55 - 11:35)'
		s3 = f'3 пара (12:15 - 13:55)'
		s4 = f'4 пара (14:10 - 15:50)'
		s5 = f'5 пара (16:20 - 18:00)'
		o1 = f''
		if p11 == p12:
			if p11 == "!":
				s1 = f'{s1}\nНа расслабоне, на чиле\n'
			else:
				s1 = f'{s1}\n{p11}\n'
		else:
			s1 = f'{s1}\n{p11} | {p12},\n'
		if p21 == p22:
			if p21 == "!":
				s2 = f'{s2}\nНа расслабоне, на чиле\n'
			else:
				s2 = f'{s2}\n{p21}\n'
		else:
			s2 = f'{s2}\n{p21} | {p22}\n'
		if p31 == p32:
			if p31 == "!":
				s3 = f'{s3}\nНа расслабоне, на чиле\n'
			else:
				s3 = f'{s3}\n{p31}\n'
		else:
			s3 = f'{s3}\n{p31} | {p32}\n'
		if p41 == p42:
			if p41 == "!":
				s4 = f'{s4}\nНа расслабоне, на чиле\n'
			else:
				s4 = f'{s4}\n{p41}\n'
		else:
			s4 = f'{s4}\n{p41} | {p42}\n'
		if p51 == p52:
			if p51 == "!":
				s5 = f'{s5}\nНа расслабоне, на чиле\n'
			else:
				s5 = f'{s5}\n{p51}\n'
		else:
			s5 = f'{s5}\n{p51} | {p52}\n'
		o = f'{d}\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}'
		print (o)
		bot.send_message(message.chat.id,text = o)
		bot.register_next_step_handler(message,day);
	elif message.text == "Четверг":
		worksheet = sh.worksheet(f"{week}")
		p11 = worksheet.acell('C24').value
		p12 = worksheet.acell('D24').value
		p21 = worksheet.acell('C25').value
		p22 = worksheet.acell('D25').value
		p31 = worksheet.acell('C26').value
		p32 = worksheet.acell('D26').value
		p41 = worksheet.acell('C27').value
		p42 = worksheet.acell('D27').value
		p51 = worksheet.acell('C28').value
		p52 = worksheet.acell('D28').value
		d = f'Расписание на Четверг'
		s1 = f'1 пара (8:00 - 9:40)'
		s2 = f'2 пара (9:55 - 11:35)'
		s3 = f'3 пара (12:15 - 13:55)'
		s4 = f'4 пара (14:10 - 15:50)'
		s5 = f'5 пара (16:20 - 18:00)'
		o1 = f''
		if p11 == p12:
			if p11 == "!":
				s1 = f'{s1}\nНа расслабоне, на чиле\n'
			else:
				s1 = f'{s1}\n{p11}\n'
		else:
			s1 = f'{s1}\n{p11} | {p12},\n'
		if p21 == p22:
			if p21 == "!":
				s2 = f'{s2}\nНа расслабоне, на чиле\n'
			else:
				s2 = f'{s2}\n{p21}\n'
		else:
			s2 = f'{s2}\n{p21} | {p22}\n'
		if p31 == p32:
			if p31 == "!":
				s3 = f'{s3}\nНа расслабоне, на чиле\n'
			else:
				s3 = f'{s3}\n{p31}\n'
		else:
			s3 = f'{s3}\n{p31} | {p32}\n'
		if p41 == p42:
			if p41 == "!":
				s4 = f'{s4}\nНа расслабоне, на чиле\n'
			else:
				s4 = f'{s4}\n{p41}\n'
		else:
			s4 = f'{s4}\n{p41} | {p42}\n'
		if p51 == p52:
			if p51 == "!":
				s5 = f'{s5}\nНа расслабоне, на чиле\n'
			else:
				s5 = f'{s5}\n{p51}\n'
		else:
			s5 = f'{s5}\n{p51} | {p52}\n'
		o = f'{d}\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}'
		print (o)
		bot.send_message(message.chat.id,text = o)
		bot.register_next_step_handler(message,day);
	elif message.text == "Пятница":
		
		worksheet = sh.worksheet(f"{week}")
		p11 = worksheet.acell('C31').value
		p12 = worksheet.acell('D31').value
		p21 = worksheet.acell('C32').value
		p22 = worksheet.acell('D32').value
		p31 = worksheet.acell('C33').value
		p32 = worksheet.acell('D33').value
		p41 = worksheet.acell('C34').value
		p42 = worksheet.acell('D34').value
		p51 = worksheet.acell('C35').value
		p52 = worksheet.acell('D35').value
		d = f'Расписание на пятницу'
		s1 = f'1 пара (8:00 - 9:40)'
		s2 = f'2 пара (9:55 - 11:35)'
		s3 = f'3 пара (12:15 - 13:55)'
		s4 = f'4 пара (14:10 - 15:50)'
		s5 = f'5 пара (16:20 - 18:00)'
		o1 = f''
		if p11 == p12:
			if p11 == "!":
				s1 = f'{s1}\nНа расслабоне, на чиле\n'
			else:
				s1 = f'{s1}\n{p11}\n'
		else:
			s1 = f'{s1}\n{p11} | {p12},\n'
		if p21 == p22:
			if p21 == "!":
				s2 = f'{s2}\nНа расслабоне, на чиле\n'
			else:
				s2 = f'{s2}\n{p21}\n'
		else:
			s2 = f'{s2}\n{p21} | {p22}\n'
		if p31 == p32:
			if p31 == "!":
				s3 = f'{s3}\nНа расслабоне, на чиле\n'
			else:
				s3 = f'{s3}\n{p31}\n'
		else:
			s3 = f'{s3}\n{p31} | {p32}\n'
		if p41 == p42:
			if p41 == "!":
				s4 = f'{s4}\nНа расслабоне, на чиле\n'
			else:
				s4 = f'{s4}\n{p41}\n'
		else:
			s4 = f'{s4}\n{p41} | {p42}\n'
		if p51 == p52:
			if p51 == "!":
				s5 = f'{s5}\nНа расслабоне, на чиле\n'
			else:
				s5 = f'{s5}\n{p51}\n'
		else:
			s5 = f'{s5}\n{p51} | {p52}\n'
		o = f'{d}\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}'
		print (o)
		bot.send_message(message.chat.id,text = o)
		bot.register_next_step_handler(message,day);
	elif message.text == "Суббота":
			
		worksheet = sh.worksheet(f"{week}")
		p11 = worksheet.acell('C38').value
		p12 = worksheet.acell('D38').value
		p21 = worksheet.acell('C39').value
		p22 = worksheet.acell('D39').value
		p31 = worksheet.acell('C40').value
		p32 = worksheet.acell('D40').value
		p41 = worksheet.acell('C41').value
		p42 = worksheet.acell('D41').value
		p51 = worksheet.acell('C42').value
		p52 = worksheet.acell('D42').value
		d = f'Расписание на субботу'
		s1 = f'1 пара (8:00 - 9:40)'
		s2 = f'2 пара (9:55 - 11:35)'
		s3 = f'3 пара (12:15 - 13:55)'
		s4 = f'4 пара (14:10 - 15:50)'
		s5 = f'5 пара (16:20 - 18:00)'
		o1 = f''
		if p11 == p12:
			if p11 == "!":
				s1 = f'{s1}\nНа расслабоне, на чиле\n'
			else:
				s1 = f'{s1}\n{p11}\n'
		else:
			s1 = f'{s1}\n{p11} | {p12}\n'
		if p21 == p22:
			if p21 == "!":
				s2 = f'{s2}\nНа расслабоне, на чиле\n'
			else:
				s2 = f'{s2}\n{p21}\n'
		else:
			s2 = f'{s2}\n{p21} | {p22}\n'
		if p31 == p32:
			if p31 == "!":
				s3 = f'{s3}\nНа расслабоне, на чиле\n'
			else:
				s3 = f'{s3}\n{p31}\n'
		else:
			s3 = f'{s3}\n{p31} | {p32}\n'
		if p41 == p42:
			if p41 == "!":
				s4 = f'{s4}\nНа расслабоне, на чиле\n'
			else:
				s4 = f'{s4}\n{p41}\n'
		else:
			s4 = f'{s4}\n{p41} | {p42}\n'
		if p51 == p52:
			if p51 == "!":
				s5 = f'{s5}\nНа расслабоне, на чиле\n'
			else:
				s5 = f'{s5}\n{p51}\n'
		else:
			s5 = f'{s5}\n{p51} | {p52}\n'
		o = f'{d}\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}'
		print (o)
		bot.send_message(message.chat.id,text = o)
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
