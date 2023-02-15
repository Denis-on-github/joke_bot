import requests
from bs4 import BeautifulSoup as BS
import random
import telebot

URL = 'https://upjoke.com/british-jokes'
API_KEY = '5744448172:AAGbdQNgtRIeZytaR-9burcnmMZCy2RrxaI'
def parser(url):
    r = requests.get(url)
    soup = BS(r.text, 'html.parser')
    jokes = soup.find_all('h3', class_='joke-title')
    return [i.text for i in jokes]

jokes_list = parser(URL)
random.shuffle(jokes_list)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, 'Hello! My name is Vitaliy, if you want to read my great jokes, give me one integer from 1 to 9:')

@bot.message_handler(content_types=['text'])

def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, jokes_list[0])
        del jokes_list[0]
    else:
        bot.send_message(message.chat.id, 'Integer from 1 to 9 please:')

bot.polling()