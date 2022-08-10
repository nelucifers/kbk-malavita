import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, ContextTypes, CommandHandler

TOKEN = '5048220651:AAET4h_9_iq0J5qcsmeUUj9qnX8EhJ_0okc'
# CHAT_ID = '5136585077'
DB = dict()


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

async def creatRecord(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    id = update.message.from_user.id
    record = list()

    if id in DB:
        record = DB[id]
    record.append(msg)    
    DB[id] = record

    print(DB)


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), creatRecord)
    
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    
    application.run_polling()