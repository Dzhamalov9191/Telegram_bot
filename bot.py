#Библиотеки, которые загружаем из вне
import telebot
#Наш Токенчик
TOKEN = 'Токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('welcome.webp', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("📄 Мое Резюме")
	item2 = types.KeyboardButton("🏞 Лендинг")
	item3 = types.KeyboardButton("⏳ Написать мне в личку")

	markup.add(item1, item2, item3)

	bot.send_message(message.chat.id, "Приветствую тебя дорогой друг, {0.first_name}!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#назначаем действие для клавиатуры
@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '📄 Мое Резюме':
			bot.send_message(message.chat.id, 'https://github.com/Dzhamalov9191/about-me')
		elif message.text == '🏞 Лендинг':
			bot.send_message(message.chat.id, 'УВЫ Лендинг пока что не готов =(')
		elif message.text == '⏳ Написать мне в личку':
			bot.send_message(message.chat.id, 'https://t.me/Dzhamalov9191')
		else:
			bot.send_message(message.chat.id, 'Не знаю что ответить😢')


bot.polling(none_stop=True)









#https://core.telegram.org/bots/api#available-methods
