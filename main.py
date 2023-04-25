import re

from telegram.ext import Updater, Filters, MessageHandler, CommandHandler 
from telegram import ReplyKeyboardMarkup

updater = Updater(token='6097495006:AAEUuOF7ILr_BDj73qob0uKaz_JC3Lg9OTQ')

def i_dont_know(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['Позвать оператора','Начнем сначала?']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id, text='Конкретизируйте свой вопрос или позовите оператора. Или может начнем сначала?',
        reply_markup=button)
    

def call_operator(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['/start']], resize_keyboard=True)
    context.bot.send_message(chat_id=chat.id, text='Пока тут нет оператора. Начнем сначала?',
        reply_markup=button)


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

def questions_about_entry(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([['Бакалавриат или специалитет', 'Магистратура'], ['Аспирантура']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id, 
        text='На какой уровень образования Вы планируете поступать?',
        reply_markup=buttons
        )

def questions_about_phd(update, context):
    chat = update.effective_chat
    button = ReplyKeyboardMarkup([['Начать сначала']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id, 
        text='Консультация по поступлению в аспирантуру пока не осуществляется. Обращайтесь по номеру телефона +7(812)328-82-80',
        reply_markup=button
        )


def questions_about_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([['Направления подготовки магистратуры'], ['Вступительные испытания в магистратуру'], ['Документы для поступления в магистратуру'], ['Сроки подачи документов', 'Способы подачи документов'], ['Списки поступающих']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id, 
        text='Что именно Вас интересует?',
        reply_markup=buttons
        )

def questions_about_specialization_magister(update, context):
    chat = update.effective_chat
    buttons = ReplyKeyboardMarkup([['План приёма в магистратуру','Информация о специальностях магистратуры'],['Назад к магистратуре']], resize_keyboard=True)
    context.bot.send_message(
        chat_id=chat.id, 
        text='Предлагаем ознакомиться с количеством мест при приёме в магистратуру, а также получить информацию об образовательных программах',
        reply_markup=buttons
        )

def questions_about_KCP_magister(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id, 
        text='Информация о количестве мест опубликована по ссылке: https://priem.spmi.ru/sites/default/files/manager/03.PlanPriema/kcp_mag.pdf',
        )

def questions_about_landing_magister(update, context):
    chat = update.effective_chat
    context.bot.send_message(
        chat_id=chat.id, 
        text='Подробная информация о количестве мест собрана на сайте: http://landing.spmi.ru/magistratura',
        )


dict={
    r'оператор':call_operator,
    r'здравствуйте|сначала|привет':wake_up,
    r'План приёма в магистратуру':questions_about_KCP_magister,
    r'Информация о специальностях магистратуры':questions_about_landing_magister,
    r'Направления подготовки магистратуры':questions_about_specialization_magister,
    r'магистратур|Назад к магистратуре':questions_about_magister,
    r'аспирантур':questions_about_phd,
    r'Хочу узнать про поступление':questions_about_entry,
    r'заявление на общежитие':questions_about_application_for_hostel,
    r'Цены и виды комфортности':questions_about_price_hostel,
    r'Идентификационный':questions_about_identificate_number,
    r'общежитие':questions_about_hostel,
    }    


updater.dispatcher.add_handler(CommandHandler('start', wake_up))


for a in dict:
    updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(a, re.IGNORECASE)), dict[a]))


#updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(a, re.IGNORECASE)), wake_up))
#updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'оператор', re.IGNORECASE)), dict['оператор']))
#updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'привет', re.IGNORECASE)), wake_up))
# updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'здравствуйте', re.IGNORECASE)), wake_up))
# updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'сначала', re.IGNORECASE)), wake_up))
# updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'заявление на общежитие', re.IGNORECASE)), questions_about_application_for_hostel))
# updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'Цены и виды комфортности', re.IGNORECASE)), questions_about_price_hostel))
# updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'общежитие', re.IGNORECASE)), questions_about_hostel))
# updater.dispatcher.add_handler(MessageHandler(Filters.regex(re.compile(r'Идентификационный', re.IGNORECASE)), questions_about_identificate_number))
updater.dispatcher.add_handler(MessageHandler(Filters.text, i_dont_know))
# Метод start_polling() запускает процесс polling, 
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling()
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
updater.idle() 