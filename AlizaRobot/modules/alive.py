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
  TEXT = f"**Heyâ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nI am ðð¥ð¢ð³ðâ**\nâââââââ¦âà¼»à¼ºââ¦ââââââ\n\n"
  TEXT += f"**à¼ï¸** **My Creatorâ : [ââââââ âªâ¬â®â®â®â® âââââªâ¬â®â®â®â® âââðââÊÎ±ÆÆÏ ââ ðââ âªâ¬â®â®â®â® ââââ](https://t.me/sakku_cute)** \n\n"
  TEXT += f"**à¼ï¸** **PTB Version :** `{telever}` \n\n"
  TEXT += f"**à¼ï¸** **Python Version :** `{python_version()}` \n\n"
  TEXT += f"**à¼ï¸** **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"**à¼ï¸** **Pyrogram Version :** `{pyrover}`\n\n"
  TEXT += f"**à¼ï¸** **Core :** `{psutil.cpu_percent()}%` \n\n"
  TEXT += f"**à¼ï¸** **Platform :** `Ubuntu Linux`\n\n"
  TEXT += f"**à¼ï¸** **Aliza Version :** `2.1.0`\nâââââââ¦âà¼»à¼ºââ¦ââââââ\n\n"
  BUTTON = [[Button.url("Supportâ", "https://t.me/Aliza_support"), Button.url("Developer", f"https://t.me/sakku_cute")]]
  ran = random.choice(PHOTO)
  await tbot.send_file(event.chat_id, ran, caption=TEXT,  buttons=BUTTON)

## Alive mod
