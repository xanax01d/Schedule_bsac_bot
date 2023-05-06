


#					█████████████████████████████████████████████████████████████████████████████   █
#					█████████████████████████████████████████████████████████   ██████   ████████   █
#					█   ███   ████   █████   █   ██████   █████   ███   ███   ██   ████   ███████   █
#					███  █   ███   ██   ███   ██   ██   ██   ████  █   ██   █████   ███   ███   █   █
#					████  █████   ███   ███   ██   █   ███   █████  █████   ██████   ██   ██  ███   █
#					██  ██   ██   ███   ███   ██   █   ███   ███  ██   ███   ████   ███   ██  ███   █
#					█   ███   ███   █    █    ██   ███   █    █   ███   █████    █████     ██   █   █
#					█████████████████████████████████████████████████████████████████████████████████ 



import datetime #для просчета недели (файл week.py)
import telebot #подключаем библиотеку для создания ботов 
from telebot import types #импортируем типы для создания клавиатуры в боте
import sqlite3 #подключаем библиотеку для использования баз данных
import week #используем внешний скрипт для просчета недель
from time import sleep

base = sqlite3.connect('bot_base.db',check_same_thread = False) #подключаем базу
cursor = base.cursor()
cursor2 = base.cursor()
cursor3 = base.cursor()
bot = telebot.TeleBot('6082835173:AAHhHhrGjGbZoL_PKXNu820m0yQKBNkNtQ0') #токен бота (при создании в @botfather получаем)
#далее идут листы групп (при переходе на след.курс менять тут и в refetch_manual)
gr_list_1course_sso = ['ИК - 211','ПО - 211','ПО - 212','РО - 211','ТО - 211','ТО - 212','ТЭ - 211','ТЭ - 212'] 
gr_list_2course_sso = ['ИК - 111','ПО - 111','ПО - 112','ПО - 221','РО - 111','ТО - 111','ТО - 112','ТР - 221','ТЭ - 111','ТЭ - 112','ТЭ - 221'] 
gr_list_3course_sso = ['ПО - 011','ПО - 012','ПО - 121','РО - 011','ТО - 011','ТО - 012','ТР - 121','ТЭ - 011','ТЭ - 012','ТЭ - 121'] 
gr_list_4course_sso = ['ПО - 021','ТЭ - 021']
gr_list_sso = gr_list_1course_sso + gr_list_2course_sso + gr_list_3course_sso + gr_list_4course_sso
gr_list_1course_vo = ['СП - 291','ИТ - 291','ИП - 291','МС - 291']
gr_list_2course_vo = ['СП - 191','ИТ - 191','МС - 191','СТ - 241','СО - 241','ИТ - 241','ПС - 241']
gr_list_3course_vo = ['СП - 091','СП - 141','МС - 091','СО - 141','СТ - 141','ИТ - 141','ПС - 141']
gr_list_4course_vo = ['СП - 041','СТ - 041','ИТ - 041','ПС - 041','СО - 041']
gr_list_vo = gr_list_1course_vo + gr_list_2course_vo + gr_list_3course_vo + gr_list_4course_vo
table_list_1course_sso = ['schedule_ik211','schedule_po211','schedule_po212','schedule_ro211','schedule_to211','schedule_to212','schedule_te211','schedule_te212'] 
table_list_2course_sso = ['schedule_ik111','schedule_po111','schedule_po112','schedule_po221','schedule_ro111','schedule_to111','schedule_to112','schedule_tr221','schedule_te111','schedule_te112','schedule_te221'] #верно
table_list_3course_sso = ['schedule_po011','schedule_po012','schedule_po121','schedule_ro011','schedule_to011','schedule_to012','schedule_tr121','schedule_te011','schedule_te012','schedule_te121'] #верно
table_list_4course_sso = ['schedule_po021','schedule_te021']
table_list_sso = table_list_1course_sso + table_list_2course_sso + table_list_3course_sso + table_list_4course_sso
table_list_1course_vo = ['schedule_sp291','schedule_it291','schedule_ip291','schedule_ms291']
table_list_2course_vo = ['schedule_sp191','schedule_it191','schedule_ms191','schedule_st241','schedule_so241','schedule_it241','schedule_ps241']
table_list_3course_vo = ['schedule_sp091','schedule_sp141','schedule_ms091','schedule_so141','schedule_st141','schedule_it141','schedule_ps141']
table_list_4course_vo = ['schedule_sp041','schedule_st041','schedule_it041','schedule_ps041','schedule_so041']
table_list_vo = table_list_1course_vo + table_list_2course_vo + table_list_3course_vo + table_list_4course_vo
table_list = table_list_sso + table_list_vo
gr_list = gr_list_sso + gr_list_vo
dict1 = dict(zip(gr_list, table_list))
l_d = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']
user_id = 0
user_group = ''
data_row = ''
sc = ''
gr = ''

def db_add_user(user_id:int,user_group:str,user_level:str,username:str,user_fn:str):
	cursor.execute(f"SELECT user_id FROM users_group WHERE user_id = {user_id}")
	data = cursor.fetchone()
	if data is None:
		cursor.execute("INSERT or REPLACE into users_group VALUES (?,?,?,?,?);",(user_id,user_group,user_level,username,user_fn))
		base.commit()
	else:
		cursor.execute("REPLACE into users_group VALUES(?,?,?,?,?);",(user_id,user_group,user_level,username,user_fn))
		base.commit()

@bot.message_handler(commands=['start']) #реакция бота на команду /start
def start(message): 
	cursor.execute("""CREATE TABLE IF NOT EXISTS users_group(
		user_id INTEGER PRIMARY KEY NOT NULL,
		user_group TEXT
		user_level TEXT
		username TEXT
		user_fn TEXT
		)""")
	base.commit()
	markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
	btn1 = types.KeyboardButton("ВО")
	btn2 = types.KeyboardButton("ССО")
	markup.add(btn1,btn2)
	bot.send_message(message.chat.id, text="Добро пожаловать в расписание академии!".format(message.from_user))
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
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("1 курс")
		btn2 = types.KeyboardButton("2 курс")
		btn3 = types.KeyboardButton("3 курс")
		btn4 = types.KeyboardButton("4 курс")
		markup.add(btn1,btn2,btn3,btn4)
		bot.send_message(message.chat.id, text="Выберите курс,на котором вы обучаетесь".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,coursesso);
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,level);
@bot.message_handler(content_types=['text'])
def coursesso(message):
	if (message.text == "1 курс"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton(gr_list_1course_sso[0])
		btn2 = types.KeyboardButton(gr_list_1course_sso[1])
		btn3 = types.KeyboardButton(gr_list_1course_sso[2])
		btn4 = types.KeyboardButton(gr_list_1course_sso[3])
		btn5 = types.KeyboardButton(gr_list_1course_sso[4])
		btn6 = types.KeyboardButton(gr_list_1course_sso[5])
		btn7 = types.KeyboardButton(gr_list_1course_sso[6])
		btn8 = types.KeyboardButton(gr_list_1course_sso[7])
		btn9 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif (message.text == "2 курс"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton(gr_list_2course_sso[0])
		btn2 = types.KeyboardButton(gr_list_2course_sso[1])
		btn3 = types.KeyboardButton(gr_list_2course_sso[2])
		btn4 = types.KeyboardButton(gr_list_2course_sso[3])
		btn5 = types.KeyboardButton(gr_list_2course_sso[4])
		btn6 = types.KeyboardButton(gr_list_2course_sso[5])
		btn7 = types.KeyboardButton(gr_list_2course_sso[6])
		btn8 = types.KeyboardButton(gr_list_2course_sso[7])
		btn9 = types.KeyboardButton(gr_list_2course_sso[8])
		btn10 = types.KeyboardButton(gr_list_2course_sso[9])
		btn11 = types.KeyboardButton(gr_list_2course_sso[10])
		btn12 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11,btn12)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif (message.text == "3 курс"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton(gr_list_3course_sso[0])
		btn2 = types.KeyboardButton(gr_list_3course_sso[1])
		btn3 = types.KeyboardButton(gr_list_3course_sso[2])
		btn4 = types.KeyboardButton(gr_list_3course_sso[3])
		btn5 = types.KeyboardButton(gr_list_3course_sso[4])
		btn6 = types.KeyboardButton(gr_list_3course_sso[5])
		btn7 = types.KeyboardButton(gr_list_3course_sso[6])
		btn8 = types.KeyboardButton(gr_list_3course_sso[7])
		btn9 = types.KeyboardButton(gr_list_3course_sso[8])
		btn10 = types.KeyboardButton(gr_list_3course_sso[9])
		btn11 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8,btn9,btn10,btn11)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif (message.text == "4 курс"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton(gr_list_4course_sso[0])
		btn2 = types.KeyboardButton(gr_list_4course_sso[1])
		btn3 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif message.text == "Назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,level);
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,level);
@bot.message_handler(content_types=['text'])
def course(message):
	if (message.text == "1 курс"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton(gr_list_1course_vo[0])
		btn2 = types.KeyboardButton(gr_list_1course_vo[1])
		btn3 = types.KeyboardButton(gr_list_1course_vo[2])
		btn4 = types.KeyboardButton(gr_list_1course_vo[3])
		btn5 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif (message.text == "2 курс"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton(gr_list_2course_vo[0])
		btn2 = types.KeyboardButton(gr_list_2course_vo[1])
		btn3 = types.KeyboardButton(gr_list_2course_vo[2])
		btn4 = types.KeyboardButton(gr_list_2course_vo[3])
		btn5 = types.KeyboardButton(gr_list_2course_vo[4])
		btn6 = types.KeyboardButton(gr_list_2course_vo[5])
		btn7 = types.KeyboardButton(gr_list_2course_vo[6])
		btn8 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7,btn8)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif (message.text == "3 курс"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton(gr_list_3course_vo[0])
		btn2 = types.KeyboardButton(gr_list_3course_vo[1])
		btn3 = types.KeyboardButton(gr_list_3course_vo[2])
		btn4 = types.KeyboardButton(gr_list_3course_vo[3])
		btn5 = types.KeyboardButton(gr_list_3course_vo[4])
		btn6 = types.KeyboardButton(gr_list_3course_vo[5])
		btn7 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5,btn6,btn7)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif (message.text == "4 курс"):
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton(gr_list_4course_vo[0])
		btn2 = types.KeyboardButton(gr_list_4course_vo[1])
		btn3 = types.KeyboardButton(gr_list_4course_vo[2])
		btn4 = types.KeyboardButton(gr_list_4course_vo[3])
		btn5 = types.KeyboardButton(gr_list_4course_vo[4])
		btn6 = types.KeyboardButton("Назад")
		markup.add(btn1,btn2,btn3,btn4,btn5,btn6)
		bot.send_message(message.chat.id, text="Выберите свою группу", reply_markup=markup)
		bot.register_next_step_handler(message,group);
	elif message.text == "Назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,level);
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,level);
@bot.message_handler(content_types=['text'])
def group(message):
	global s
	gr = message.text
	if gr in gr_list_sso:
		us_lv = "ССО"
		us_fn = message.from_user.first_name
		usn = message.from_user.username
		us_id = message.from_user.id
		db_add_user(user_id = us_id,user_group = gr,user_level = us_lv,username = usn,user_fn = us_fn);
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
	elif gr in gr_list_vo:
		us_lv = "ВО"
		us_fn = message.from_user.first_name
		usn = message.from_user.username
		us_id = message.from_user.id
		db_add_user(user_id = us_id,user_group = gr,user_level = us_lv,username = usn,user_fn = us_fn);
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
	elif message.text == 'Назад':
		markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,level);
@bot.message_handler(content_types=['text'])
def day(message):
	global sh
	global worksheet
	us_id = message.from_user.id
	cursor2.execute(f"SELECT user_group FROM users_group WHERE user_id = {us_id}")
	gr:str = ""
	gr_row = cursor2.fetchall();
	gr = '' + gr_row[0][0]
	table = dict1.get(gr)
	cursor3.execute(f'SELECT sc FROM {table}')
	schedule = cursor3.fetchall()
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
		btn1 = types.KeyboardButton("ВО")
		btn2 = types.KeyboardButton("ССО")
		markup.add(btn1,btn2)
		bot.send_message(message.chat.id, text="Выберите cтупень образования, на которой вы обучаетесь: (ВО/ССО)".format(message.from_user), reply_markup=markup)
		bot.register_next_step_handler(message,level);
bot.polling(non_stop = True)