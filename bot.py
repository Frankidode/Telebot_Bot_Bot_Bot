from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from settings import TOKEN
from phrases import *
import random as rn
from PIL import Image
img = Image.open(r'images_mem.jpeg')


def sms(bot,update):
    print('Кто-то отправил /start Что делать?')
    bot.message.reply_text(f'Здравствуйте, {bot.message.chat.first_name}, я бот!\n\
    Из возможных функций я могу вам предложить: пока только пособолезнуйте🥺')
    print(bot.message)

def memas(bot, update):
    bot.message.reply_photo('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTPZuDbLEFATlFvmdhcTO2RDtSzWg-B1v59LB5coUSCBW58BXaTYsximkAAMQ2AUaB1RvI&usqp=CAU')

def otvetka(bot, update):
    mes = bot.message.text.lower()
    print(mes)
    if mes in hello_user:
        bot.message.reply_text(rn.choice(hello_bot)+", "+rn.choice(appeal_bot))
    elif mes in appeal_user:
        bot.message.reply_text('ЧЁ?')
    elif mes in bye_user:
        bot.message.reply_text(rn.choice(bye_bot))
    else:
        bot.message.reply_text('Я вась не панимат!')


def main():
    my_bot = Updater(TOKEN)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    my_bot.dispatcher.add_handler(CommandHandler('mem', memas))

    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, otvetka))

    my_bot.start_polling()  # проверяет наличие сообщений
    my_bot.idle()  # будет работать, пока его не остановят

main()
