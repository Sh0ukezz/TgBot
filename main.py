import telebot
from telebot import types
import requests

TOKEN = '6379215281:AAFPo56nnrDu0m0-QHQpefRiACdABYGc-2A'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    itembtn_download = types.KeyboardButton('☞Скачати')
    itembtn_help = types.KeyboardButton('★Допомога')
    itembtn_contacts = types.KeyboardButton('✉Контакти')
    itembtn_invite = types.KeyboardButton('долучитися до команди')
    markup.add(itembtn_download, itembtn_help, itembtn_contacts, itembtn_invite)

    bot.send_message(message.chat.id, "Привіт! Це - телеграм бот від розробників гри The Master Of Dungeons. Щоб дізнатись інформацію про функціонал боту напишіть '/help'", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == '☞Скачати')
def send_download_link(message):
    # Логіка для відправки посилання на скачування файлу
    download_link = 'ПОСИЛАННЯ_НА_ВАШ_ФАЙЛ'
    bot.send_message(message.chat.id, f"Отримайте посилання на скачування гри: {download_link}")

@bot.message_handler(func=lambda message: message.text == '✉Контакти')
def send_contacts(message):
    # Логіка для відправки контактної інформації
    bot.send_message(message.chat.id, "Розробники: @shoukezz | @tvadimm | @im_coderrr | @Spol1t | @Emmeraldio | @litvinchuk853")

@bot.message_handler(func=lambda message: message.text.lower() == 'долучитися до команди')
def send_invite(message):
    # Логіка для відправки інформації про долучення до команди
    bot.send_message(message.chat.id, "На жаль, зараз немає вільних місць.")

@bot.message_handler(func=lambda message: message.text == '★Допомога')
def send_help(message):
    # Логіка для відправки допомоги
    bot.send_message(message.chat.id, "/help - допомога. /контакти - контактна інформація. /долучитись до команди - надіслати заявку до команди розробників. /завантажити - отримати посилання на завантаження гри.")

bot.polling()
