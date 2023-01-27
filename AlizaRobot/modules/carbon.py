from pyrogram.types import Message
from pyrogram import filters
from AlizaRobot import pbot
from AlizaRobot.utils.errors import capture_err
from AlizaRobot.utils.functions import make_carbon


@pbot.on_message(filters.command("carbon"))
@capture_err
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text("`Reply to a text to generate carbon.`")
    if not message.reply_to_message.text:
        return await message.reply_text("`Reply to a text to generate carbon.`")
    m = await message.reply_text("`Generating Carbon 🔄`")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Uploading Generated Carbon...`")
    await pbot.send_photo(message.chat.id, carbon)
    await m.delete()
    carbon.close()


__mod_name__ = "Carbon"

__help__ = """

Uploads a carbon of the replied text.

❍ /carbon *:* Uploads carbon in reply to a text.

 """
