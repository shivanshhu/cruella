"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് /start ചെയ്തു നോക്ക്..🙂" 
REPO = "not open"
CHANNEL = "Cʜᴏᴏsᴇ ʏᴏᴜʀ ʟᴀɴɢᴜᴀɢᴇs ᴍᴏᴠɪᴇs ᴄʜᴀɴɴᴇʟ Aɴᴅ ᴊᴏɪɴ ғᴀsᴛ ➦/n/n✦ ᴇɴɢʟɪsʜ (ʜᴏʟʟʏᴡᴏᴏᴅ) : https://t.me/+TFyDaeLsoDM0Y2Y1/n/n✦ ʜɪɴᴅɪ :  https://t.me/+1jquABsI3m1lYTVl/n/n✦ ᴛᴀᴍɪʟ :  https://t.me/+nzlsdKjoWRJiZjll/n/n✦ ᴛᴇʟᴜɢᴜ :  https://t.me/+hQzXQkChv0NjNWVl/n/n✦ ᴍᴀʟᴀʏᴀʟᴀᴍ :  https://t.me/+MetDlLy1mdNkZGM1/n/n✦ ᴘᴜɴᴊᴀʙɪ :  https://t.me/+v4B4-nNJyH4zZjVl/n/n✦ ᴋᴀɴɴᴀᴅᴀ : https://t.me/+6eKNZQWoj-4xOGQ1"
AJAX = "<b>𝙱𝙾𝚃 ›› https://t.me/cruella_robot</b>"
# -- Constants End -- #


@Client.on_message(filters.command("alive", COMMAND_HAND_LER) & f_onw_fliter)
async def check_alive(_, message):
    await message.reply_text(ALIVE)


@Client.on_message(filters.command("ping", COMMAND_HAND_LER) & f_onw_fliter)
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")


@Client.on_message(filters.command("rrepo", COMMAND_HAND_LER) & f_onw_fliter)
async def repo(_, message):
    await message.reply_text(REPO)


@Client.on_message(filters.command("ggroup", COMMAND_HAND_LER) & f_onw_fliter)
async def group(_, message):
    await message.reply_text(GROUP)


@Client.on_message(filters.command("channel", COMMAND_HAND_LER) & f_onw_fliter)
async def channel(_, message):
    await message.reply_text(CHANNEL)


@Client.on_message(filters.command("champu", COMMAND_HAND_LER) & f_onw_fliter)
async def ajax(_, message):
    await message.reply_text(AJAX)
