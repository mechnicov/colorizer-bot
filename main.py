#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from colorization.colorize import colorize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level = logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("Hi! Send black and white photo to me, I'll try to colorize it for you")

def main():
    updater = Updater(os.getenv('BOT_TOKEN'), use_context = True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('help', start))
    dp.add_handler(MessageHandler(Filters.photo, process))
    dp.add_handler(MessageHandler(Filters.document.category('image'), process))

    updater.start_polling()
    updater.idle()

def process(update, context):
    photo = update.message.photo[-1] if update.message.photo else update.message.document

    photo_file = photo.get_file()

    file_extension = f".{photo_file.file_path.split('.')[-1]}"

    logger.info(photo_file.file_path)

    filename = f"./photos/{photo.file_unique_id}{file_extension}"
    colorized_filename = filename.replace(file_extension , f"_colorized{file_extension}")

    photo_file.download(filename)

    colorize(filename, colorized_filename)

    colorized_photo = open(colorized_filename, 'rb')
    update.message.reply_photo(colorized_photo)
    colorized_photo.close()

if __name__ == '__main__':
    main()
