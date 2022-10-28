"""Telegram Ping / Pong Speed
Syntax: .ping"""

import time
import random
from pyrogram import Client, filters
from info import COMMAND_HAND_LER
from plugins.helper_functions.cust_p_filters import f_onw_fliter

# -- Constants -- #
ALIVE = "╔══════ ≪ •❈• ≫ ══════╗
 
   𝐇ᴀᴍ 𝐓ᴏ  𝐒ʜᴀᴜᴋ 𝐓ᴀʟᴠᴀʀᴏ
    𝐊ᴇ 𝐏ᴀʟᴀ 𝐊ᴀʀᴛᴇ 𝐇ᴀɪ 🤟🔥

   𝐁ᴀɴᴅᴜᴋᴏ 𝐊ɪ 𝐉ɪᴅᴅ 𝐓ᴏ 
   𝐁ᴀᴄʜʜᴇ 𝐊ɪʏᴀ 𝐊ᴀʀᴛᴇ 𝐇ᴀɪ 😏🖕

   𝐒ʜᴇʀ 𝐀ᴘɴᴀ 𝐒ʜɪᴋᴀʀ 𝐊ᴀʀᴛᴇ 𝐇ᴀɪ 
   𝐀ᴜʀ 𝐇ᴀᴍ 𝐀ᴘɴᴇ 𝐀ᴛᴛɪᴛᴜᴅᴇ 
   𝐒ᴇ 𝐕ᴀᴀʀ 𝐊ᴀʀᴛᴇ 𝐇ᴀɪ 🔥🔥

╚══════ ≪ •❈• ≫ ══════" 
REPO = "not open"
CHANNEL = "<b>𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻</b> ›› https://m.youtube.com/channel/UCjIQaZpHMwddQ9R0aGzME0w\n\n<b>𝚄𝙿𝙳𝙰𝚃𝙴𝚂 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/MoviesLinks00</b>\n\n<b>𝙲𝙷𝙰𝙽𝙽𝙴𝙻 ›› https://t.me/+0U4jWzUglCdlZWFl</b>"
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
