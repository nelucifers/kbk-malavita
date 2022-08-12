import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler
import datetime as dt
from time import sleep
from DatetimeParser import parser
from Event import event

TOKEN = '5048220651:AAET4h_9_iq0J5qcsmeUUj9qnX8EhJ_0okc'
CHAT_ID = '5136585077'
DB = dict()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def today(update: Update, context: ContextTypes.DEFAULT_TYPE):
    Event = event()
    events = Event.getEventsToday()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=events, parse_mode='HTML')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def creatEvent(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    message_id = update.message.message_id
    dtParser = parser(text)
    datetimeEvent = dtParser.getDateTime()
    textEvent = dtParser.getTextEvent()
    Event = event()
    Event.insert(message_id, datetimeEvent, textEvent)
    print(Event.select())


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    start_handler = CommandHandler('today', today)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), creatEvent)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling()

    now = dt.datetime.now()
    curHour = now.hour
    curHinute = now.minute
    print(f'Time: {curHour}:{curHinute}')
    # if curHour == _hour and curHinute == _minute:
    if curHour == 15 and curHinute == 21:
        Event = event()
        events = Event.getEventsToday()
        print(events)
        today(events)
        sleep(60)
    # sleep(30)