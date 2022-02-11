import shutil, psutil
import signal
import os
import asyncio



from pyrogram import idle, filters, types, emoji
from sys import executable
from quoters import Quote
import threading



from telegram import ParseMode, InlineKeyboardButton
from telegram.ext import Filters, InlineQueryHandler, MessageHandler, CommandHandler, CallbackQueryHandler, CallbackContext
from telegram.utils.helpers import escape_markdown
from telegraph import Telegraph



from wserver import start_server_async
from bot import bot, IMAGE_URL, app, dispatcher, updater, botStartTime, IGNORE_PENDING_REQUESTS, IS_VPS, PORT, alive, web, nox, OWNER_ID, AUTHORIZED_CHATS, telegraph_token, BOT_NO
from bot.helper.ext_utils import fs_utils
from bot.helper.telegram_helper.bot_commands import BotCommands
from bot.helper.telegram_helper.message_utils import *
from .helper.ext_utils.bot_utils import get_readable_file_size, get_readable_time




from .helper.telegram_helper.filters import CustomFilters
from bot.helper.telegram_helper import button_build
from .modules.rssfeeds import rss_init
from .modules import (
authorize, list, cancel_mirror, mirror_status, mirror, clone, watch, shell, eval, torrent_search, delete, speedtest, count, rssfeeds, leech_settings, search, mediainfo, updates, config, look
)







def start(update, context):
    buttons = button_build.ButtonMaker()
    buttons.buildbutton("Repo", "https://github.com/tiktikimelbo7/universal-mirror")
    reply_markup = InlineKeyboardMarkup(buttons.build_menu(1))
    if CustomFilters.authorized_user(update) or CustomFilters.authorized_chat(update):
        start_string = f'''
This bot can mirror all your links to Google Drive!
Type /{BotCommands.HelpCommand} to get a list of available commands
'''
        update.effective_message.reply_photo(IMAGE_URL, start_string, parse_mode=ParseMode.HTML)
    else:
        sendMarkup(
            'Oops! not a Authorized user.\nPlease deploy your own <b>priiiiyo-mirror-leech-bot</b>.',
            context.bot,
            update,
            reply_markup,
        )



