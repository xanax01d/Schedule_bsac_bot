import sqlite3
import gspread
from week import return_week
from time import sleep

l_d = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']
weekn = return_week()
week = ''
gr_list = ['ИТ - 291','СП - 291']
gc = gspread.service_account(filename = 'telegram-383417-054a31246b9f.json') #токен для подключения библиотеки к созданному приложению 
it291_sh = '1jH0cCxM1obOCuA7phpZf1o9IidFpsGLPR3McIgoMoUU' #ключ на расписание ИТ-291
sp291_sh = '1fejVj9VbSRilj6U5sRhxNhf2itkgDtbx0k2xDwp_vqg' #ключ на расписание СП-291
base = sqlite3.connect('bot_base.db',check_same_thread = False) #подключаем базу
cursor = base.cursor()
cursor.execute("""DROP TABLE IF EXISTS schedule_it291;""")
cursor.execute("""DROP TABLE IF EXISTS schedule_sp291;""")
base.commit()
if weekn == 1: 
	week = '1 неделя' #если первая ,открываем лист с названием "1 неделя"
if weekn == 2:
	week = '2 неделя' #если вторая,открываем лист с названием "2 неделя"
if weekn == 3:
	week = '3 неделя' #если третья,открываем лист с названием "3 неделя"
if weekn == 4:
	week = '4 неделя' #если четвертая,открываем лист с названием "4 неделя"

def create(gr):
	if gr == 'ИТ - 291':
		cursor.execute("""CREATE TABLE IF NOT EXISTS schedule_it291(
					day TEXT NOT NULL,
					sc TEXT
					)""")
		base.commit();
		print('Created schedule for',gr)
	elif gr == 'СП - 291':
		cursor.execute("""CREATE TABLE IF NOT EXISTS schedule_sp291(
				day TEXT NOT NULL,
				sc TEXT 
				)""")
		base.commit();
		print('Created schedule for',gr)
	
def save(gr,day,sc):
	if gr == "ИТ - 291":
		cursor.execute(f"SELECT sc FROM schedule_it291 WHERE day = '{day}'")
		cursor.execute("INSERT INTO schedule_it291 VALUES (?,?);",(day,sc))
		base.commit();
		print('Saved...')
	elif gr == "СП - 291":
		cursor.execute(f"SELECT sc FROM schedule_sp291 WHERE day = '{day}'")
		cursor.execute("INSERT INTO schedule_sp291 VALUES (?,?);",(day,sc))
		base.commit();
		print('Saved...')

def refetch():
	global sc
	for i in range(len(gr_list)): 
		gr = gr_list[i]
		create(gr)
		for i in range(len(l_d)):
			day = l_d[i];
			print(day)
			if gr == "ИТ - 291":
				sh = gc.open_by_key(it291_sh)
				print(gr)
				cursor.execute(f"SELECT sc FROM schedule_it291 WHERE day = '{day}'")
				base.commit()
				data_row = cursor.fetchone()
				print (data_row)
			elif gr == "СП - 291":
				sh = gc.open_by_key(sp291_sh)
				print(gr)
				cursor.execute(f"SELECT sc FROM schedule_sp291 WHERE day = '{day}'")
				base.commit()
				data_row = cursor.fetchone()
				print (data_row)
			if data_row is None:
				if day == 'Понедельник':
					wc1 = 'C3'
					wd1 = 'D3'
					wc2 = 'C4'
					wd2 = 'D4'
					wc3 = 'C5'
					wd3 = 'D5'
					wc4 = 'C6'
					wd4 = 'D6'
					wc5 = 'C7'
					wd5 = 'D8'
				elif day == 'Вторник':
					wc1 = 'C10'
					wd1 = 'D10'
					wc2 = 'C11'
					wd2 = 'D11'
					wc3 = 'C12'
					wd3 = 'D12'
					wc4 = 'C13'
					wd4 = 'D13'
					wc5 = 'C14'
					wd5 = 'D14'
				elif day == 'Среда':
					wc1 = 'C17'
					wd1 = 'D17'
					wc2 = 'C18'
					wd2 = 'D18'
					wc3 = 'C19'
					wd3 = 'D19'
					wc4 = 'C20'
					wd4 = 'D20'
					wc5 = 'C21'
					wd5 = 'D21'
				elif day == 'Четверг':
					wc1 = 'C24'
					wd1 = 'D24'
					wc2 = 'C25'
					wd2 = 'D25'
					wc3 = 'C26'
					wd3 = 'D26'
					wc4 = 'C27'
					wd4 = 'D27'
					wc5 = 'C28'
					wd5 = 'D28'
				elif day == 'Пятница':
					wc1 = 'C31'
					wd1 = 'D31'
					wc2 = 'C32'
					wd2 = 'D32'
					wc3 = 'C33'
					wd3 = 'D33'
					wc4 = 'C34'
					wd4 = 'D34'
					wc5 = 'C35'
					wd5 = 'D35'
				elif day == 'Суббота':
					wc1 = 'C38'
					wd1 = 'D38'
					wc2 = 'C39'
					wd2 = 'D39'
					wc3 = 'C40'
					wd3 = 'D40'
					wc4 = 'C41'
					wd4 = 'D41'
					wc5 = 'C42'
					wd5 = 'D42'
				worksheet = sh.worksheet(f"{week}")
				p11 = worksheet.acell(wc1).value
				p12 = worksheet.acell(wd1).value
				p21 = worksheet.acell(wc2).value
				p22 = worksheet.acell(wd2).value
				p31 = worksheet.acell(wc3).value
				p32 = worksheet.acell(wd3).value
				p41 = worksheet.acell(wc4).value
				p42 = worksheet.acell(wd4).value
				p51 = worksheet.acell(wc5).value
				p52 = worksheet.acell(wd5).value
				s1 = f'1 пара (8:00 - 9:40)'
				s2 = f'2 пара (9:55 - 11:35)'
				s3 = f'3 пара (12:15 - 13:55)'
				s4 = f'4 пара (14:10 - 15:50)'
				s5 = f'5 пара (16:20 - 18:00)'
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
				sc = f'\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}'
				save(gr,day,sc)
				sleep(10);
refetch()