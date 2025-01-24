with open('.config', 'r') as file:
    TOKEN = file.readline()

from telegram import *
from telegram.ext import *
import requests as rq

def img(animal:str):
    response = rq.get(f'https://some-random-api.com/img/{animal}')
    data = response.json()
    if response.status_code == 200:
        image_url = data['link']
    return image_url

async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Hi! With my help you can send animal pictures to chat without any problems!')


async def animalBird(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img('bird'))

async def animalCar(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img('cat'))

async def animalDog(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img('dog'))

async def animalFox(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img('fox'))

async def animalRedPanda(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img('red_panda'))

async def animalPanda(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=img('panda'))


if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help))
    app.add_handler(CommandHandler('bird', animalBird))
    app.add_handler(CommandHandler('cat', animalCar))
    app.add_handler(CommandHandler('dog', animalDog))
    app.add_handler(CommandHandler('fox', animalFox))
    app.add_handler(CommandHandler('red_panda', animalRedPanda))
    app.add_handler(CommandHandler('panda', animalPanda))
    app.run_polling()
