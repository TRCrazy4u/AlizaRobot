import speedtest
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CallbackQueryHandler, run_async

from AlizaRobot import DEV_USERS, dispatcher
from AlizaRobot.modules.disable import DisableAbleCommandHandler
from AlizaRobot.modules.helper_funcs.chat_status import dev_plus


def convert(speed):
    return round(int(speed) / 1048576, 2)


@dev_plus
@run_async
def speedtestxyz(update: Update, context: CallbackContext):
    buttons = [
        [
            InlineKeyboardButton("𝐈𝐦𝐚𝐠𝐞", callback_data="speedtest_image"),
            InlineKeyboardButton("𝐓𝐞𝐱𝐭", callback_data="speedtest_text"),
        ]
    ]
    update.effective_message.reply_text(
        "Choose a Speedtest Mode in Aliza", reply_markup=InlineKeyboardMarkup(buttons)
    )


@run_async
def speedtestxyz_callback(update: Update, context: CallbackContext):
    query = update.callback_query

    if query.from_user.id in DEV_USERS: 
        msg = update.effective_message.edit_text("Running a speedtest..🔄")
        speed = speedtest.Speedtest()
        speed.get_best_server()
        speed.download()
        speed.upload()
        replymsg = "𝐒𝐩𝐞𝐞𝐝𝐭𝐞𝐬𝐭 𝐑𝐞𝐬𝐮𝐥𝐭 𝐨𝐟 𝐀𝐥𝐢𝐳𝐚"

        if query.data == "speedtest_image":
            speedtest_image = speed.results.share()
            update.effective_message.reply_photo(
                photo=speedtest_image, caption=replymsg
            )
            msg.delete()

        elif query.data == "speedtest_text":
            result = speed.results.dict()
            replymsg += f"\n𝐃𝐨𝐰𝐧𝐥𝐨𝐚𝐝: `{convert(result['download'])}Mb/s`\n𝐔𝐩𝐥𝐨𝐚𝐝: `{convert(result['upload'])}Mb/s`\n𝐏𝐢𝐧𝐠: `{result['ping']}`"
            update.effective_message.edit_text(replymsg, parse_mode=ParseMode.MARKDOWN)
    else:
        query.answer("You are required to join @Aliza_support to use this command.")


SPEED_TEST_HANDLER = DisableAbleCommandHandler("speedtest", speedtestxyz)
SPEED_TEST_CALLBACKHANDLER = CallbackQueryHandler(
    speedtestxyz_callback, pattern="speedtest_.*"
)

dispatcher.add_handler(SPEED_TEST_HANDLER)
dispatcher.add_handler(SPEED_TEST_CALLBACKHANDLER)

__help__ = """
*⚠️ Notice:*
*(For Devs Only)*
❍ /speedtest *:* Runs a speedtest and check the server speed.
"""

__mod_name__ = "Speedtest​"
__command_list__ = ["speedtest"]
__handlers__ = [SPEED_TEST_HANDLER, SPEED_TEST_CALLBACKHANDLER]
