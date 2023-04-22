import gspread
import telebot
from telebot import types

bot = telebot.TeleBot('6082835173:AAHhHhrGjGbZoL_PKXNu820m0yQKBNkNtQ0')
gc = gspread.service_account(filename = 'telegram-383417-aeb956c7ced6.json')

sh = gc.open("ИТ-291 | Расписание")

week = 1 
if week == 1:
	worksheet = sh.worksheet("1 неделя")
if week == 2:
	worksheet = sh.worksheet("2 неделя")
if week == 3:
	worksheet = sh.worksheet("3 неделя")
if week == 4:
	worksheet = sh.worksheet("4 неделя")

@bot.message_handler(commands=['start'])
def start(message):
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
	if message.text == "ИТ - 291":
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
	if message.text == "Понедельник":
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
		bot.send_message(message.chat.id, text="Расписание на Понедельник")
		bot.send_message(message.chat.id, text="1 пара (8:00 - 9.40)")
		if p11 == p12:
			if p11 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p11)
		else:
			bot.send_message(message.chat.id,text = f'{p11} | {p12}')
		bot.send_message(message.chat.id, text="2 пара (9:55 - 11:35)")
		if p21 == p22:
			if p21 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p21)
		else:
			bot.send_message(message.chat.id,text = f'{p21} | {p22}')
		bot.send_message(message.chat.id, text="3 пара (12:15 - 13:55)")
		if p31 == p32:
			if p31 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p31)
		else:
			bot.send_message(message.chat.id,text = f'{p31} | {p32}')
		bot.send_message(message.chat.id, text="4 пара (14:10 - 15:50)")
		if p41 == p42:
			if p41 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p41)
		else:
			bot.send_message(message.chat.id,text = f'{p41} | {p42}')
		bot.send_message(message.chat.id, text="5 пара (16:20 - 18:00)")
		if p51 == p52:
			if p51 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p51)
		else:
			bot.send_message(message.chat.id,text = f'{p51} | {p52}')
		bot.register_next_step_handler(message,day);
	elif message.text == "Вторник":
		p11 = worksheet.acell('C11').value
		p12 = worksheet.acell('D11').value
		p21 = worksheet.acell('C12').value
		p22 = worksheet.acell('D12').value
		p31 = worksheet.acell('C13').value
		p32 = worksheet.acell('D13').value
		p41 = worksheet.acell('C14').value
		p42 = worksheet.acell('D14').value
		p51 = worksheet.acell('C15').value
		p52 = worksheet.acell('D15').value
		bot.send_message(message.chat.id, text="Расписание на Вторник")
		bot.send_message(message.chat.id, text="1 пара (8:00 - 9.40)")
		if p11 == p12:
			if p11 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p11)
		else:
			bot.send_message(message.chat.id,text = f'{p11} | {p12}')
		bot.send_message(message.chat.id, text="2 пара (9:55 - 11:35)")
		if p21 == p22:
			if p21 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p21)
		else:
			bot.send_message(message.chat.id,text = f'{p21} | {p22}')
		bot.send_message(message.chat.id, text="3 пара (12:15 - 13:55)")
		if p31 == p32:
			if p31 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p31)
		else:
			bot.send_message(message.chat.id,text = f'{p31} | {p32}')
		bot.send_message(message.chat.id, text="4 пара (14:10 - 15:50)")
		if p41 == p42:
			if p41 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p41)
		else:
			bot.send_message(message.chat.id,text = f'{p41} | {p42}')
		bot.send_message(message.chat.id, text="5 пара (16:20 - 18:00)")
		if p51 == p52:
			if p51 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p51)
		else:
			bot.send_message(message.chat.id,text = f'{p51} | {p52}')
		bot.register_next_step_handler(message,day);
	elif message.text == "Среда":
		p11 = worksheet.acell('C17').value
		p12 = worksheet.acell('D17').value
		p21 = worksheet.acell('C18').value
		p22 = worksheet.acell('D18').value
		p31 = worksheet.acell('C19').value
		p32 = worksheet.acell('D19').value
		p41 = worksheet.acell('C20').value
		p42 = worksheet.acell('D20').value
		p51 = worksheet.acell('C21').value
		p52 = worksheet.acell('D21').value
		bot.send_message(message.chat.id, text="Расписание на Среду")
		bot.send_message(message.chat.id, text="1 пара (8:00 - 9.40)")
		if p11 == p12:
			if p11 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p11)
		else:
			bot.send_message(message.chat.id,text = f'{p11} | {p12}')
		bot.send_message(message.chat.id, text="2 пара (9:55 - 11:35)")
		if p21 == p22:
			if p21 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p21)
		else:
			bot.send_message(message.chat.id,text = f'{p21} | {p22}')
		bot.send_message(message.chat.id, text="3 пара (12:15 - 13:55)")
		if p31 == p32:
			if p31 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p31)
		else:
			bot.send_message(message.chat.id,text = f'{p31} | {p32}')
		bot.send_message(message.chat.id, text="4 пара (14:10 - 15:50)")
		if p41 == p42:
			if p41 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p41)
		else:
			bot.send_message(message.chat.id,text = f'{p41} | {p42}')
		bot.send_message(message.chat.id, text="5 пара (16:20 - 18:00)")
		if p51 == p52:
			if p51 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p51)
		else:
			bot.send_message(message.chat.id,text = f'{p51} | {p52}')
		bot.register_next_step_handler(message,day);
	elif message.text == "Четверг":
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
		bot.send_message(message.chat.id, text="Расписание на Четверг")
		bot.send_message(message.chat.id, text="1 пара (8:00 - 9.40)")
		if p11 == p12:
			if p11 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p11)
		else:
			bot.send_message(message.chat.id,text = f'{p11} | {p12}')
		bot.send_message(message.chat.id, text="2 пара (9:55 - 11:35)")
		if p21 == p22:
			if p21 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p21)
		else:
			bot.send_message(message.chat.id,text = f'{p21} | {p22}')
		bot.send_message(message.chat.id, text="3 пара (12:15 - 13:55)")
		if p31 == p32:
			if p31 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p31)
		else:
			bot.send_message(message.chat.id,text = f'{p31} | {p32}')
		bot.send_message(message.chat.id, text="4 пара (14:10 - 15:50)")
		if p41 == p42:
			if p41 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p41)
		else:
			bot.send_message(message.chat.id,text = f'{p41} | {p42}')
		bot.send_message(message.chat.id, text="5 пара (16:20 - 18:00)")
		if p51 == p52:
			if p51 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p51)
		else:
			bot.send_message(message.chat.id,text = f'{p51} | {p52}')
		bot.register_next_step_handler(message,day);
	elif message.text == "Пятница":
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
		bot.send_message(message.chat.id, text="Расписание на Пятницу")
		bot.send_message(message.chat.id, text="1 пара (8:00 - 9.40)")
		if p11 == p12:
			if p11 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p11)
		else:
			bot.send_message(message.chat.id,text = f'{p11} | {p12}')
		bot.send_message(message.chat.id, text="2 пара (9:55 - 11:35)")
		if p21 == p22:
			if p21 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p21)
		else:
			bot.send_message(message.chat.id,text = f'{p21} | {p22}')
		bot.send_message(message.chat.id, text="3 пара (12:15 - 13:55)")
		if p31 == p32:
			if p31 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p31)
		else:
			bot.send_message(message.chat.id,text = f'{p31} | {p32}')
		bot.send_message(message.chat.id, text="4 пара (14:10 - 15:50)")
		if p41 == p42:
			if p41 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p41)
		else:
			bot.send_message(message.chat.id,text = f'{p41} | {p42}')
		bot.send_message(message.chat.id, text="5 пара (16:20 - 18:00)")
		if p51 == p52:
			if p51 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p51)
		else:
			bot.send_message(message.chat.id,text = f'{p51} | {p52}')
		bot.register_next_step_handler(message,day);
	elif message.text == "Cуббота":
		bot.register_next_step_handler(message,day);
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
		bot.send_message(message.chat.id, text="Расписание на Субботу")
		bot.send_message(message.chat.id, text="1 пара (8:00 - 9.40)")
		if p11 == p12:
			if p11 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p11)
		else:
			bot.send_message(message.chat.id,text = f'{p11} | {p12}')
		bot.send_message(message.chat.id, text="2 пара (9:55 - 11:35)")
		if p21 == p22:
			if p21 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p21)
		else:
			bot.send_message(message.chat.id,text = f'{p21} | {p22}')
		bot.send_message(message.chat.id, text="3 пара (12:15 - 13:55)")
		if p31 == p32:
			if p31 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p31)
		else:
			bot.send_message(message.chat.id,text = f'{p31} | {p32}')
		bot.send_message(message.chat.id, text="4 пара (14:10 - 15:50)")
		if p41 == p42:
			if p41 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p41)
		else:
			bot.send_message(message.chat.id,text = f'{p41} | {p42}')
		bot.send_message(message.chat.id, text="5 пара (16:20 - 18:00)")
		if p51 == p52:
			if p51 == "-":
				bot.send_message(message.chat.id,text = "Окно")
			else:
				bot.send_message(message.chat.id,text = p51)
		else:
			bot.send_message(message.chat.id,text = f'{p51} | {p52}')
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
