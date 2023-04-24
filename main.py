from telegram.ext import Updater, Filters, MessageHandler, CommandHandler 
from telegram import ReplyKeyboardMarkup

updater = Updater(token='6097495006:AAEUuOF7ILr_BDj73qob0uKaz_JC3Lg9OTQ')

def say_hi(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='Доброго времени суток')
    
def say_not(update, context):
    chat = update.effective_chat
    context.bot.send_message(chat_id=chat.id, text='No')

def wake_up(update, context):
    chat = update.effective_chat
    name = update.message.chat.first_name
    buttons = ReplyKeyboardMarkup([['Хочу узнать про поступление', 'Хочу узнать про общежитие']])
    context.bot.send_message(
        chat_id=chat.id, 
        text='Приёмная комиссия Горного университета приветствует Вас, {}!'.format(name),
        reply_markup=buttons
        )

# Регистрируется обработчик MessageHandler;
# из всех полученных сообщений он будет выбирать только текстовые сообщения
# и передавать их в функцию say_hi()
updater.dispatcher.add_handler(CommandHandler('start', wake_up))
updater.dispatcher.add_handler(MessageHandler(Filters.text, say_hi))
updater.dispatcher.add_handler(MessageHandler(Filters.photo, say_not))
# Метод start_polling() запускает процесс polling, 
# приложение начнёт отправлять регулярные запросы для получения обновлений.
updater.start_polling()
# Бот будет работать до тех пор, пока не нажмете Ctrl-C
updater.idle() 