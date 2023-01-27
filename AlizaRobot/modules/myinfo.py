import asyncio
import datetime
import re
from datetime import datetime

from telethon import custom, events

from AlizaRobot import telethn as bot
from AlizaRobot import telethn as tgbot
from AlizaRobot.events import register

edit_time = 5
""" =======================Aliza ROBOT====================== """
file1 = "https://telegra.ph/file/6e35ad27281c52e4b12dd.png"
file2 = "https://telegra.ph/file/3d7c34a58976d2df373ac.png"
file3 = "https://telegra.ph/file/148e28b33ed55083ea00a.png"
file4 = "https://telegra.ph/file/55f60104165c934c7b24b.png"
file5 = "https://telegra.ph/file/33a80ea9c3f7dbf7038d5.png"
""" =======================Aliza ROBOT====================== """


@register(pattern="/myinfo")
async def proboyx(event):
    await event.get_chat()
    datetime.utcnow()
    firstname = event.sender.first_name
    button = [[custom.Button.inline("Information",data="informations")]]
    on = await bot.send_file(event.chat_id, file=file2,caption= f"Hey {firstname}, \n Click on the button below \n to get info about you", buttons=button)

    await asyncio.sleep(edit_time)
    ok = await bot.edit_message(event.chat_id, on, file=file3, buttons=button) 

    await asyncio.sleep(edit_time)
    ok2 = await bot.edit_message(event.chat_id, ok, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok3 = await bot.edit_message(event.chat_id, ok2, file=file1, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok4 = await bot.edit_message(event.chat_id, ok3, file=file2, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok5 = await bot.edit_message(event.chat_id, ok4, file=file1, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok6 = await bot.edit_message(event.chat_id, ok5, file=file3, buttons=button)
    
    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file5, buttons=button)

    await asyncio.sleep(edit_time)
    ok7 = await bot.edit_message(event.chat_id, ok6, file=file4, buttons=button)

@tgbot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    PRO = await bot.get_entity(boy)
    LILIE = "Powered By 𝐀𝐥𝐢𝐳𝐚 \n\n"
    LILIE += f"👤First Name : {PRO.first_name} \n"
    LILIE += f"👤Last Name : {PRO.last_name}\n"
    LILIE += f"🤖Is BOT : {PRO.bot} \n"
    LILIE += f"🔏Is Restricted : {PRO.restricted} \n"
    LILIE += f"🔖User Id : {boy}\n"
    LILIE += f"🤵Username : {PRO.username}\n"
    await event.answer(LILIE, alert=True)
  except Exception as e:
    await event.reply(f"{e}")


__command_list__ = [
    "myinfo"
]
