#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Simple Bot to reply to Telegram messages.
This program is dedicated to the public domain under the CC0 license.
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ParseMode
import logging
import apiai, json
import datetime, re, requests
import random
import urllib, urllib2

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

timestart = datetime.datetime.now()


# Define a few command handlers. These usually take the two arguments bot and
# update. Error handlers also receive the raised TelegramError object in error.
def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')



def echo(bot, update):
    """Echo the user message."""
    mes = update.message.text

    if update.message.date < timestart:
        return
    if len(mes) < 8:
        return
    if mes.find(u'Болтун,') <> 0:
        return
    mes = mes[7:].strip()


if __name__ == '__main__':
    settingsUsers = {}
    try:
        settingsUsers = loadUsers()
    except IOError as e:
        saveUsers(settingsUsers)
    main()
