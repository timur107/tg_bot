import telebot
import config
import random
from random import choice

bot = telebot.TeleBot(config.token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hello, I am BotusBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

#Число от 0 до 100    
@bot.message_handler(commands=['random', 'rnd'])
def send_welcome(message):
    number = random.randint(0, 100)
    bot.reply_to(message, "Случайное число от 0 до 100: " + str(number))

#Орел или решка 
@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["орел", "решка"])
    bot.reply_to(message, coin)

#Рандомные цитаты
@bot.message_handler(commands=['quote'])
def send_quote(message):
    quotes = ['Никакое дело не покажется невыполнимым, если разбить его на части (Генри Форд).', 'Трудности похожи на собак: они кусают лишь тех, кто к ним не привык (древнегреческий философ Антисфен).', 'Никогда не отказывайся от того, что заставляет тебя улыбаться (Хит Леджер).', 'Неважно, как медленно ты идешь, пока не останавливаешься (Конфуций).', 'Если ты можешь мечтать, то можешь воплотить свои мечты в жизнь (Уолт Дисней).']
    quote = quotes.pop(random.randint(0, 4))
    bot.reply_to(message, quote)

#Новый пользователь
@bot.message_handler(content_types=['new_chat_members'])
def make_some(message):
    bot.send_message(message.chat.id, 'I accepted a new user!')
    bot.approve_chat_join_request(message.chat.id, message.from_user.id)
    
# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, "Ты написал: " + message.text)


bot.infinity_polling()