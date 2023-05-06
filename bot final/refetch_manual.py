


#			█████████████████████████████████████████████████████████████████████████████   █
#			█████████████████████████████████████████████████████████   ██████   ████████   █
#			█   ███   ████   █████   █   ██████   █████   ███   ███   ██   ████   ███████   █
#			███  █   ███   ██   ███   ██   ██   ██   ████  █   ██   █████   ███   ███   █   █
#			████  █████   ███   ███   ██   █   ███   █████  █████   ██████   ██   ██  ███   █		      			
#			██  ██   ██   ███   ███   ██   █   ███   ███  ██   ███   ████   ███   ██  ███   █													
#			█   ███   ███   █    █    ██   ███   █    █   ███   █████    █████     ██   █   █							
#			█████████████████████████████████████████████████████████████████████████████████



import sqlite3
import gspread
import week
from time import sleep
import os
os.system('cls')  #чистим консоль
print('.▄▄ ·  ▄▄·  ▄ .▄▄▄▄ .·▄▄▄▄  ▄• ▄▌▄▄▌  ▄▄▄ .  ▄• ▄▌ ▄▄▄··▄▄▄▄   ▄▄▄· ▄▄▄▄▄▄▄▄ .▄▄▄  ')
print('▐█ ▀. ▐█ ▌▪██▪▐█▀▄.▀·██· ██ █▪██▌██•  ▀▄.▀·  █▪██▌▐█ ▄███· ██ ▐█ ▀█ •██  ▀▄.▀·▀▄ █·')
print('▄▀▀▀█▄██ ▄▄██▀▀█▐▀▀▪▄▐█▪ ▐█▌█▌▐█▌██ ▪ ▐▀▀▪▄  █▌▐█▌ ██▀·▐█▪ ▐█▌▄█▀▀█  ▐█.▪▐▀▀▪▄▐▀▀▄ ')
print('▐█▄▪▐█▐███▌██▌▐▀▐█▄▄▌██. ██ ▐█▄█▌▐█▌ ▄▐█▄▄▌  ▐█▄█▌▐█▪·•██. ██ ▐█▪ ▐▌ ▐█▌·▐█▄▄▌▐█•█▌')
print(' ▀▀▀▀ ·▀▀▀ ▀▀▀ · ▀▀▀ ▀▀▀▀▀•  ▀▀▀ .▀▀▀  ▀▀▀    ▀▀▀ .▀   ▀▀▀▀▀•  ▀  ▀  ▀▀▀  ▀▀▀ .▀  ▀')
#54 группы 
#далее идут листы групп (при переходе на след.курс менять тут и в боте) (либо просто меняете тут и копируете в бота) таблицы и ключи к гуглам в том же порядке,как и группы,иначе устанете потом в бд править)
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
table_list_2course_sso = ['schedule_ik111','schedule_po111','schedule_po112','schedule_po221','schedule_ro111','schedule_to111','schedule_to112','schedule_tr221','schedule_te111','schedule_te112','schedule_te221']
table_list_3course_sso = ['schedule_po011','schedule_po012','schedule_po121','schedule_ro011','schedule_to011','schedule_to012','schedule_tr121','schedule_te011','schedule_te012','schedule_te121'] 
table_list_4course_sso = ['schedule_po021','schedule_te021']
table_list_sso = table_list_1course_sso + table_list_2course_sso + table_list_3course_sso + table_list_4course_sso
table_list_1course_vo = ['schedule_sp291','schedule_it291','schedule_ip291','schedule_ms291']
table_list_2course_vo = ['schedule_sp191','schedule_it191','schedule_ms191','schedule_st241','schedule_so241','schedule_it241','schedule_ps241']
table_list_3course_vo = ['schedule_sp091','schedule_sp141','schedule_ms091','schedule_so141','schedule_st141','schedule_it141','schedule_ps141']
table_list_4course_vo = ['schedule_sp041','schedule_st041','schedule_it041','schedule_ps041','schedule_so041']
table_list_vo = table_list_1course_vo + table_list_2course_vo + table_list_3course_vo + table_list_4course_vo
sh_list_1course_sso = ['1HnpnyOc2ZWKB5rOsjKW3Yt5jzeVtrOtuyxJfEuzGPj4','1--hMnWd25v-k_0fbNrEN62QBJHj6dkGdOyOzcTxOHdc','18fMsnMuWlu1eYdCMgnB0jBglpie6oBEGOwAjv-_vCaw','1z_IW-J59oX5vDcqmQufVLhcUUaBqFTZhX-GtvVVI4ps','1TEJg6VYomHvStKzkkL4PhpwVpM91fryU8e1LHILr26o','1QRhYkK3yIc2iZQ5OxFH0Q84VJjQ4D_c-hB01OqAN6Qw','1jHYSYtXeJpXDsukQZ7Jqm0O51U_TECzwoeA6MOHUfRE','1JXOLNVmb8r_oRwRAcPaGVZWeCrOgt23dTW2vhw67GBc']
sh_list_2course_sso = ['1iMh2xH9RD2hI3oE82tgXmNJsZFnE2I7K2jK7Ov_WRXc','13JjATlgn6yTbFK-yai1KW3jzMdC_FQML8vGJFT6jkHY','1SB_j_ZdShMFwuK4BzXiy5zDCz3HiTC7X3WAUVm4NlZ0','1SbbJQsCnhOfJ013ymEK4vx_c3hwW9XrauBqQKrP5v0w','15kfMDMRtA_a876srW3JytDRjSuJokDfpyAYPQkJyafM','1iXPJzmrcymuN9kQvHuFafI8dSDt6253B5_Papdem1BE','1CDeJY9p8qUd7eapykFS5QeqLY3hL8nK0mUnvKXD5nb4','1YePx8DVjxqZZLCywAGWYZYwzlWOv2w4gfQPhruB0Zzc','1qLMo42RWxwmfX7qGNE29EldMGEENe7Jx5a74doc9CDM','1wLQd0TaCxkuKvQ9acO4CNx-tk1XK7u5N3AeMsj8bfwk','13lbbdFUugxrI-IJakkdUiSvSrJuKt1daKQHLRhW7Mnw']
sh_list_3course_sso = ['1oAbsJcRCfPpDqM4UIEs9F4dR95cnSwxDMK-U5PHU56I','1NKMABamF2lSEptLBNhSel6TekJtV3Mu0FceUKDktKfM','1BUOH3GB0ZEv0u_2Is8EP2I3SP8pL0oo4LtFuh802KkM','1_baCTaLPXO_2OrbCmJ-pIuoNn_T_tf120dT12Aopous','1F3mO91SYcGlIrfQ8t8PdAIKQcThkcbaxrDihwUji0MM','1XMloFzhneGBU37jp4kdZ6sbB_Pk3jFlSvlSVXCmGV5A','1XMloFzhneGBU37jp4kdZ6sbB_Pk3jFlSvlSVXCmGV5A','1ZumB69aqFHigFGDZmspxuApyQRNL547z_Qs3r6NeyzA','1C3-O5d49n2sCx7dlVkFGoDXuG3qRiw7vDfDyvArogc4','1bryLepjzXWu4tbFYuDe1RrYEOhFy3R1i678FiO7-_7g']
sh_list_4course_sso = ['10I1f500jzuAWFDPCi8w8IhT6hTdgI79ZzF_coIa6e9E','1p_50FQsDIqb8_lFTQ0iy0JQQqa9H4kj_-WaZigI23F8']
sh_list_1course_vo = ['1fejVj9VbSRilj6U5sRhxNhf2itkgDtbx0k2xDwp_vqg','1jH0cCxM1obOCuA7phpZf1o9IidFpsGLPR3McIgoMoUU','1UPNcDqKxFzsw2cj54XN9RX4hgTh7b5qGuvgfRocIXMg','1dPLKOxezuw2FM68fchaodWwazZueP8ElEAiXnuFGvD8']
sh_list_2course_vo = ['1Hv8EI1ZoO2TqbRkZamlOTJ3V5_Y3IlWlezdkfkwysjw','1dxNHCuqPvR9Yp5yBI8eC9AWqANNmTxBckyzDD0VUK3c','1J7WbV-vKTyaB0iIioHfdnvema9gJ6YPPlakljunoJlc','1tV3d2y_WGqYCO3MBAl-iXkSajZ_0RFEFFwU7RdfASsc','1Cca8TmqEdfjgEzg8txMWMzKe_2thCprHZbBkh-uVXn4','1jeDZfHgQCMB_dhaVHsAY0ItCvOp57NLwHvG7QTZ2nUU','1eGJKIPO57WUHOS68sbYZB9iEUcOATMKc_4bTVH3ZERo']
sh_list_3course_vo = ['1QKdj7Jdl6hrnRDyCLwIL6nvkloS2C0bhJdpE8EPe2i0','1jSrcI-Y2iqlGoRpQln-YVtkcrzM9y3mUP9Zpx8_k_Nc','1JLL0sd68iDbdYmO1VEY3pGRjByMdiul7JfpXBKQY8H0','1md1zb5p9Wu_tpOEJ9V7ppetWg-X2yxAzQsNbibJE1wc','1pmD1Tr59useXCoXjEFzrv9mZxLSolxzgXTfEkzwvV9s','1MgZoeKuRhxw-94mqPPkNmzx5AKgxThZAnNoFD4BkHcg','1oDzS_q55WjLyZBtzl8Dx6Gap_EnQmE42cgL24NfBkgE']
sh_list_4course_vo = ['1ZFkRTglIMjS-veVgZqt1TDTv2mhMXQnnRDr20A125TU','1PKJQeMG6DWf8KgN5cRF8h7tJoERnn4wp8d08TLNdbCU','10B6ApET2nxdPEMcvBE2UitFXk9Kzn_s_YLO4TpmDhZs','12il-mfNZSQeGWuoFC5YTLBY53TIbxgUEIVESUAFW3ng','1JyJfbqHFWzHZvHGHnXLjaqIncJ5RwGpWGV_Im0GHw1w']
sh_list_vo = sh_list_1course_vo + sh_list_2course_vo + sh_list_3course_vo + sh_list_4course_vo
sh_list_sso = sh_list_1course_sso + sh_list_2course_sso + sh_list_3course_sso + sh_list_4course_sso
l_d = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']
weekn = 1
week = ''
gr_list = gr_list_sso + gr_list_vo
table_list = table_list_sso + table_list_vo
shs = sh_list_sso + sh_list_vo
dict1 = dict(zip(gr_list, table_list))
dict2 = dict(zip(table_list , shs))
gc = gspread.service_account(filename = 'telegram-383417-241753d7248f.json') #токен для подключения библиотеки к созданному приложению 
base = sqlite3.connect('bot_base.db',check_same_thread = False) #подключаем базу
cursor = base.cursor()
base.commit()
if weekn == 1: 
	week = '1 неделя' #если первая ,открываем лист с названием "1 неделя"
if weekn == 2:
	week = '2 неделя' #если вторая,открываем лист с названием "2 неделя"
if weekn == 3:
	week = '3 неделя' #если третья,открываем лист с названием "3 неделя"
if weekn == 4:
	week = '4 неделя' #если четвертая,открываем лист с названием "4 неделя"
def deleting():
	for i in range(len(table_list)):
		tablename = table_list[i]
		cursor.execute(f'DROP TABLE IF EXISTS {tablename};')
		base.commit();
def create():
	for i in range(len(table_list)):
		tablename = table_list[i]
		cursor.execute(f'CREATE TABLE IF NOT EXISTS {tablename}('
					'day TEXT NOT NULL,'
					'sc TEXT'
					')')
		base.commit();
def save(gr,day,sc):
	if gr in gr_list:
		s = dict1.get(gr)
		cursor.execute(f"SELECT sc FROM {s} WHERE day = '{day}'")
		cursor.execute(f"INSERT INTO {s} VALUES (?,?);",(day,sc))
		base.commit();
def refetch():
	global sc
	for i in range(len(gr_list)): 
		gr = gr_list[i]
		s = dict1.get(gr)
		sd = dict2.get(s)
		for i in range(len(l_d)):
			day = l_d[i];
			sh = gc.open_by_key(sd)
			cursor.execute(f"SELECT sc FROM {s} WHERE day = '{day}'")
			base.commit()
			data_row = cursor.fetchone()
			if data_row is None:
				if day == 'Понедельник':
					wc = 'C3:D8'
				elif day == 'Вторник':
					wc = 'C10:D15'
				elif day == 'Среда':
					wc = 'C17:D22'
				elif day == 'Четверг':
					wc = 'C24:D29'
				elif day == 'Пятница':
					wc = 'C31:D36'
				elif day == 'Суббота':
					wc = 'C38:D43'
				worksheet = sh.worksheet(f"{week}")
				d = worksheet.get(wc)
				p11 = d[0][0]
				p12 = d[0][1]
				p21 = d[1][0]
				p22 = d[1][1]
				p31 = d[2][0]
				p32 = d[2][1]
				p41 = d[3][0]
				p42 = d[3][1]
				p51 = d[4][0]
				p52 = d[4][1]
				p61 = d[5][0]
				p62 = d[5][1]
				s1 = f'1 пара (8:00 - 9:40)'
				s2 = f'2 пара (9:55 - 11:35)'
				s3 = f'3 пара (12:15 - 13:55)'
				s4 = f'4 пара (14:10 - 15:50)'
				s5 = f'5 пара (16:20 - 18:00)'
				s6 = f'6 пара (18:15 - 19:55)'
				if p11 == p12:
					if p11 == "!":
						s1 = f'{s1}\nОкно\n'
					else:
						s1 = f'{s1}\n{p11}\n'
				else:
					s1 = f'{s1}\n{p11} | {p12}\n'
				if p21 == p22:
					if p21 == "!":
						s2 = f'{s2}\nОкно\n'
					else:
						s2 = f'{s2}\n{p21}\n'
				else:
					s2 = f'{s2}\n{p21} | {p22}\n'
				if p31 == p32:
					if p31 == "!":
						s3 = f'{s3}\nОкно\n'
					else:
						s3 = f'{s3}\n{p31}\n'
				else:
					s3 = f'{s3}\n{p31} | {p32}\n'
				if p41 == p42:
					if p41 == "!":
						s4 = f'{s4}\nОкно\n'
					else:
						s4 = f'{s4}\n{p41}\n'
				else:
					s4 = f'{s4}\n{p41} | {p42}\n'
				if p51 == p52:
					if p51 == "!":
						s5 = f'{s5}\nОкно\n'
					else:
						s5 = f'{s5}\n{p51}\n'
				else:
					s5 = f'{s5}\n{p51} | {p52}\n'
				if p61 == p62:
					if p61 == "!":
						s6 = f'{s6}\nОкно\n'
					else:
						s6 = f'{s6}\n{p61}\n'
				else:
					s6 = f'{s6}\n{p61} | {p62}\n'
				sc = f'\n{s1}\n{s2}\n{s3}\n{s4}\n{s5}\n{s6}'
				save(gr,day,sc)
				d.clear()
				sleep (5)
		print('The weekly schedule is saved for the group: ',gr)
		sleep(10)
deleting()
create()
refetch()