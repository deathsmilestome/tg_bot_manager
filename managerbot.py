from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot)

async def on_startup(_):
	print('Started')
##################################Кнопки меню###########################

### создание главного меню###
main1 = KeyboardButton('-|О нас')
main2 = KeyboardButton('-|Площадки')
main3 = KeyboardButton('-|Активности')

main_client = ReplyKeyboardMarkup(resize_keyboard=True)
#main_client.add(main1).add(main2).add(main3) #.insert() .row(, ,)
main_client.row(main1,main2,main3)
### меню активностей###
act1 = InlineKeyboardButton(text='Пейнтбол', callback_data='act1')
act2 = InlineKeyboardButton(text='Лазертаг', callback_data='act2')
act3 = InlineKeyboardButton(text='Квест', callback_data='act3')

act_client = InlineKeyboardMarkup(row_width=1)
#act_client.add(act1).add(act2).add(act3)
act_client.row(act1,act2,act3)
##################################Client################################
@dp.message_handler(commands=['start'])
async def command_start(message : types.Message):
	start=open('description/start.txt',encoding="utf-8")
	await message.answer(start.read(), reply_markup=main_client)
	start.close()

### главное меню ###
@dp.message_handler(text_contains='-|')
async def about_us(message :types.Message):
	if message.text == '-|О нас':
		about=open('description/about.txt',encoding="utf-8")
		await message.answer(about.read())
		about.close()
	if message.text == '-|Площадки':
		place1=open('description/place1.txt',encoding="utf-8")
		photosKorkino = types.MediaGroup()
		photosKorkino.attach_photo(types.InputFile('photos/Korkino/1.jpg'), '1')
		photosKorkino.attach_photo(types.InputFile('photos/Korkino/2.jpg'), '2')
		photosKorkino.attach_photo(types.InputFile('photos/Korkino/3.jpg'), '3')
		photosKorkino.attach_photo(types.InputFile('photos/Korkino/4.jpg'), '4')
		photosKorkino.attach_photo(types.InputFile('photos/Korkino/5.jpg'), '5')
		photosKorkino.attach_photo(types.InputFile('photos/Korkino/6.jpg'), '6')
		place2=open('description/place2.txt',encoding="utf-8")
		photosLazure = types.MediaGroup()
		photosLazure.attach_photo(types.InputFile('photos/Lazure/1.jpg'), '1')
		photosLazure.attach_photo(types.InputFile('photos/Lazure/2.jpg'), '2')
		photosLazure.attach_photo(types.InputFile('photos/Lazure/3.jpg'), '3')
		photosLazure.attach_photo(types.InputFile('photos/Lazure/4.jpg'), '4')
		await message.answer(place1.read())
		await bot.send_media_group(message.chat.id, media=photosKorkino)
		await message.answer(place2.read())
		await bot.send_media_group(message.chat.id, media=photosLazure)
		place1.close()
		place2.close()
	if message.text == '-|Активности':
		acts=open('description/acts.txt',encoding="utf-8")
		await message.answer(acts.read(), reply_markup=act_client)
		acts.close()		
	
### ловим ответ о выборе активности ###
@dp.callback_query_handler(text_contains='act')
async def act(callback : types.CallbackQuery):
	if callback.data == 'act1':
		act1=open('description/paintball.txt',encoding="utf-8")
		photosPaintball = types.MediaGroup()
		photosPaintball.attach_photo(types.InputFile('photos/Paintball/1.jpg'), '1')
		photosPaintball.attach_photo(types.InputFile('photos/Paintball/2.jpg'), '2')
		photosPaintball.attach_photo(types.InputFile('photos/Paintball/3.jpg'), '3')
		photosPaintball.attach_photo(types.InputFile('photos/Paintball/gun.jpg'), 'gun')
		photosPaintball.attach_photo(types.InputFile('photos/Paintball/mask.jpg'), 'mask')
		await callback.message.answer(act1.read(), reply_markup=act_client)
		await bot.send_media_group(callback.message.chat.id, media=photosPaintball)
		act1.close()
	if callback.data == 'act2':
		act2=open('description/lazertag.txt',encoding="utf-8")
		photosLazertag = types.MediaGroup()
		photosLazertag.attach_photo(types.InputFile('photos/Lazertag/1.jpg'), '1')
		photosLazertag.attach_photo(types.InputFile('photos/Lazertag/2.jpg'), '2')
		photosLazertag.attach_photo(types.InputFile('photos/Lazertag/3.jpg'), '3')
		photosLazertag.attach_photo(types.InputFile('photos/Lazertag/gun1.png'), 'gun')
		photosLazertag.attach_photo(types.InputFile('photos/Lazertag/gun2.png'), 'gun')
		await callback.message.answer(act2.read(), reply_markup=act_client)
		await bot.send_media_group(callback.message.chat.id, media=photosLazertag)
		act2.close()
	if callback.data == 'act3':
		act3=open('description/quest.txt',encoding="utf-8")
		photosQuest = types.MediaGroup()
		photosQuest.attach_photo(types.InputFile('photos/Quest/1.jpg'), '1')
		photosQuest.attach_photo(types.InputFile('photos/Quest/2.jpg'), '2')
		photosQuest.attach_photo(types.InputFile('photos/Quest/3.jpg'), '3')
		await callback.message.answer(act3.read(), reply_markup=act_client)
		await bot.send_media_group(callback.message.chat.id, media=photosQuest)
		act3.close()
	await callback.answer('')	
####################################Admin###############################
### кнопки редактирования ###
admin1 = InlineKeyboardButton(text='Стартовое сообщение', callback_data='admin1')
admin2 = InlineKeyboardButton(text='О нас', callback_data='admin2')
admin3 = InlineKeyboardButton(text='Площадка1', callback_data='admin3')
admin4 = InlineKeyboardButton(text='Площадка2', callback_data='admin4')
admin5 = InlineKeyboardButton(text='Активности', callback_data='admin5')
admin6 = InlineKeyboardButton(text='Пейнтбол', callback_data='admin6')
admin7 = InlineKeyboardButton(text='Лазертаг', callback_data='admin7')
admin8 = InlineKeyboardButton(text='Квест', callback_data='admin8')


admin_menu = InlineKeyboardMarkup(row_width=1)
admin_menu.add(admin1).add(admin2).add(admin3).add(admin4).add(admin5).add(admin6).add(admin7).add(admin8)

### Кнопка отмены ###
cancel= InlineKeyboardButton(text='Отмена', callback_data='cancel')
cancel_button= InlineKeyboardMarkup ().add(cancel)

### вход для админа и редакция текста ###
@dp.message_handler(text_contains='Who is your daddy, Mr robot ?')
async def admin(message :types.Message):
	admins = [431821127, 123124] #ivan,#
	if message.from_user.id in admins :
		await message.answer('Приветствую, мастер!')
		await message.answer('Что будем менять ?',reply_markup = admin_menu)
	else :
		await message.answer('Точно не ты 🤨')

### выбор файла для редактирования ###
	global status 
	global file 
@dp.callback_query_handler(text_contains='admin')
async def act(callback : types.CallbackQuery):
	global status 
	global file 
	status = False
	if callback.data == 'admin1':
		status=True
		file='start'
		await callback.message.answer("!!! РЕДАКТИРОВАНИЕ -Стартовое сообщение !!! \nОтправь новый текст, если передумал, жми отмену", reply_markup=cancel_button)

		
	if callback.data == 'admin2':
		status=True
		file='about'
		await callback.message.answer("!!! РЕДАКТИРОВАНИЕ -О нас !!! \nОтправь новый текст, если передумал, жми отмену", reply_markup=cancel_button)
	
	if callback.data == 'admin3':
		status=True
		file='place1'
		await callback.message.answer("!!! РЕДАКТИРОВАНИЕ -Площадка1 !!! \nОтправь новый текст, если передумал, жми отмену", reply_markup=cancel_button)	

	if callback.data == 'admin4':
		status=True
		file='place2'
		await callback.message.answer("!!! РЕДАКТИРОВАНИЕ -Площадка2 !!! \nОтправь новый текст, если передумал, жми отмену", reply_markup=cancel_button)

	if callback.data == 'admin5':
		status=True
		file='acts'
		await callback.message.answer("!!! РЕДАКТИРОВАНИЕ -Активности !!! \nОтправь новый текст, если передумал, жми отмену", reply_markup=cancel_button)

	if callback.data == 'admin6':
		status=True
		file='paintball'
		await callback.message.answer("!!! РЕДАКТИРОВАНИЕ -Пейнтбол !!! \nОтправь новый текст, если передумал, жми отмену", reply_markup=cancel_button)
		
	if callback.data == 'admin7':
		status=True
		file='lazertag'
		await callback.message.answer("!!! РЕДАКТИРОВАНИЕ -Лазертаг !!! \nОтправь новый текст, если передумал, жми отмену", reply_markup=cancel_button)		
	
	if callback.data == 'admin8':
		status=True
		file='quest'
		await callback.message.answer("!!! РЕДАКТИРОВАНИЕ -Квест !!! \nОтправь новый текст, если передумал, жми отмену", reply_markup=cancel_button)

	await callback.answer('')

### Отмена ###		
@dp.callback_query_handler(text_contains='cancel')
async def act(callback : types.CallbackQuery):
	global status 
	await callback.message.answer('Хоршо, ничего не меняем')
	status=False
	await callback.answer('')

### процесс редактирования ###

@dp.message_handler()
async def redact_process(message :types.Message):
	global status 
	global file 
	if status==True:
		start_redact= open ('description/'+file+'.txt','w',encoding="utf-8")
		start_redact.write(message.text)
		start_redact.close()
		status=False

###################################ALL##################################
@dp.message_handler()
async def echo_sen(message :types.Message):
	if message.text == '+':
		await message.answer('IVAN')



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
