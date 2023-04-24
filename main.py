import re

from telegram.ext import Updater, Filters, MessageHandler, CommandHandler 
from telegram import ReplyKeyboardMarkup

updater = Updater(token='6097495006:AAEUuOF7ILr_BDj73qob0uKaz_JC3Lg9OTQ')

def i_dont_know(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['Позвать оператора']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id, text='Конкретизируйте свой вопрос или позовите оператора',
        reply_markup=button)
    

def call_operator(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['/start']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id, text='Пока тут нет оператора. Начнем сначала?',
        reply_markup=button)

def say_not(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='No')

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([['Хочу узнать про поступление', 'Хочу узнать про общежитие']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id, 
        text='Приёмная комиссия Горного университета приветствует Вас, {}!'.format(name),
        reply_markup=buttons
        )
    
def questions_about_hostel(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([['Цены и виды комфортности', 'Как и когда подавать заявление на общежитие?'], ['Как узнать свой идентификационный номер?']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id, 
        text='Что именно Вас интересует?',
        reply_markup=buttons
        )

def questions_about_identificate_number(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id, 
        text='Данную информацию можете получить по ссылке: https://priem.spmi.ru/abiurient-nomer'
        )

def questions_about_application_for_hostel(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id, 
        text='Данную информацию можете получить по ссылке: https://priem.spmi.ru/sites/default/files/manager/obzhezhitia/2022/Poryadok_predost.pdf'
        )

def questions_about_price_hostel(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id, 
        text='Данную информацию можете получить по ссылке: https://spmi.ru/stoimost-prozivania-s-ucetom-komfortnosti'
        )
    
updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'оператор', re.IGNORECASE)), call_operator))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'привет', re.IGNORECASE)), wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'здравствуйте', re.IGNORECASE)), wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'заявление на общежитие', re.IGNORECASE)), questions_about_application_for_hostel))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'Цены и виды комфортности', re.IGNORECASE)), questions_about_price_hostel))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'общежитие', re.IGNORECASE)), questions_about_hostel))
updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'Идентификационный', re.IGNORECASE)), questions_about_identificate_number))
updater.dispatcher.add_handler(MessageHandler(Filters.text, i_dont_know))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, say_not))
# Метод start_polling() запускает процесс polling, 
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling()
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
updater.idle() 