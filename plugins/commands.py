"""
radio player, Telegram Voice Chat Userbot
Copyright (C) 2021  youtubeslgeekshow

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import Client, filters
import signal
from utils import USERNAME, FFMPEG_PROCESSES, mp
from config import Config
import os
import sys
U=USERNAME
CHAT=Config.CHAT
msg=Config.msg
HOME_TEXT = "<b> ðº Hello, [{}](tg://user?id={})\n\n I am 24Ã7 Non Stop Radio/Music Player ð .\n\n Hits /help for more details...</b>"
HELP = """
**ð· Common Commands â»ï¸**
â·/play **[song name]/[yt link]**: Reply to an audio file.
â·/dplay **[song name]:** Play music from Deezer.
â·/player:  Show current playing song.
â·/help: Show help for commands.
â·/playlist: Shows the playlist.

**ð· Group Admin Commands ð°**
â·/skip **[n]** ...  Skip current or n where n >= 2
â·/join: Join voice chat.
â·/leave: Leave current voice chat
â·/vc: Check which VC is joined.
â·/stop: Stop playing.
â·/radio: Start Radio.
â·/stopradio: Stops Radio Stream.
â·/replay: Play from the beginning.
â·/clean: Remove unused RAW PCM files.
â·/pause: Pause playing.
â·/resume: Resume playing.
â·/mute: Mute in VC.
â·/unmute: Unmute in VC.
â·/restart: Restarts the Bot.
"""



@Client.on_message(filters.command(['start', f'start@{U}']))
async def start(client, message):
    buttons = [
        [
        InlineKeyboardButton("ð¦socure code ð¦ ", url='https://github.com/youtubeslgeekshow/radioplayer-bot'),
    ],
    [
        InlineKeyboardButton('ð Bot update Channel', url='https://t.me/sl_bot_zone'),
        InlineKeyboardButton('ð¨âð» Bot support group', url='https://t.me/slbotzone'),
    ],
    [
        InlineKeyboardButton('ð  Help & Commands ð ', callback_data='help'),

    ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    await message.delete()



@Client.on_message(filters.command(["help", f"help@{U}"]))
async def show_help(client, message):
    buttons = [
        [
            InlineKeyboardButton("ð¦socure code ð¦ ", url='https://github.com/youtubeslgeekshow/radioplayer-bot'),
        ],
        [
            InlineKeyboardButton('ð Bot update Channel', url='https://t.me/sl_bot_zone'),
            InlineKeyboardButton('ð¨âð» Bot support group', url='https://t.me/slbotzone'),
        ],
        [
            InlineKeyboardButton('ð¨âð»Developer ', url='https://t.me/supunma'),
        
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(
        HELP,
        reply_markup=reply_markup
        )
    await message.delete()
@Client.on_message(filters.command(["restart", f"restart@{U}"]) & filters.user(Config.ADMINS))
async def restart(client, message):
    await message.reply_text("ð Restarting...")
    await message.delete()
    process = FFMPEG_PROCESSES.get(CHAT)
    if process:
        process.send_signal(signal.SIGTERM) 
    os.execl(sys.executable, sys.executable, *sys.argv)
    
