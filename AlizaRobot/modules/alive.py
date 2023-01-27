import os
import re, psutil
import random
from platform import python_version 
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from AlizaRobot.events import register
from AlizaRobot import telethn as tbot


PHOTO = [
    "https://telegra.ph/file/f1a09a66af60178dd7dae.jpg",
]

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hey​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nI am 𝐀𝐥𝐢𝐳𝐚​**\n┏━━━━━✦❘༻༺❘✦━━━━━┓\n\n"
  TEXT += f"**༒︎** **My Creator​ : [‌‌‌‌≛⃝ ⁪⁬⁮⁮⁮⁮ ‌‌‌‌⁪⁬⁮⁮⁮⁮ ‌‌‌👑≛⃝ʂαƙƙυ ≛⃝ 👑≛⃝ ⁪⁬⁮⁮⁮⁮ ‌‌‌‌](https://t.me/sakku_cute)** \n\n"
  TEXT += f"**༒︎** **PTB Version :** `{telever}` \n\n"
  TEXT += f"**༒︎** **Python Version :** `{python_version()}` \n\n"
  TEXT += f"**༒︎** **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"**༒︎** **Pyrogram Version :** `{pyrover}`\n\n"
  TEXT += f"**༒︎** **Core :** `{psutil.cpu_percent()}%` \n\n"
  TEXT += f"**༒︎** **Platform :** `Ubuntu Linux`\n\n"
  TEXT += f"**༒︎** **Aliza Version :** `2.1.0`\n┗━━━━━✦❘༻༺❘✦━━━━━┛\n\n"
  BUTTON = [[Button.url("Support​", "https://t.me/Aliza_support"), Button.url("Developer", f"https://t.me/sakku_cute")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
