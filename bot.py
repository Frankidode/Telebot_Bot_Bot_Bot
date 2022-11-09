from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TOKEN

def sms(bot,update):
    print('Кто-то отправил /start Что делать?')
    bot.message.reply_text(f'Здравствуйте, {bot.message.chat.first_name}, я бот!\nПока я еще ничего не умею, но я быстро учусь!🥺')
    print(bot.message)

def parrot(bot, update):
    print(bot.message.text)
    bot.message.reply_text(bot.message.text)


def main():
    my_bot = Updater(TOKEN)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))

    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

    my_bot.start_polling()  # проверяет наличие сообщений
    my_bot.idle()  # будет работать, пока его не остановят

main()
