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
            InlineKeyboardButton("šš¦šš š", callback_data="speedtest_image"),
            InlineKeyboardButton("ššš±š­", callback_data="speedtest_text"),
        ]
    ]
    update.effective_message.reply_text(
        "Choose a Speedtest Mode in Aliza", reply_markup=InlineKeyboardMarkup(buttons)
    )


@run_async
def speedtestxyz_callback(update: Update, context: CallbackContext):
    query = update.callback_query

    if query.from_user.id in DEV_USERS: 
        msg = update.effective_message.edit_text("Running a speedtest..š")
        speed = speedtest.Speedtest()
        speed.get_best_server()
        speed.download()
        speed.upload()
        replymsg = "šš©šššš­šš¬š­ ššš¬š®š„š­ šØš šš„š¢š³š"

        if query.data == "speedtest_image":
            speedtest_image = speed.results.share()
            update.effective_message.reply_photo(
                photo=speedtest_image, caption=replymsg
            )
            msg.delete()

        elif query.data == "speedtest_text":
            result = speed.results.dict()
            replymsg += f"\nššØš°š§š„šØšš: `{convert(result['download'])}Mb/s`\nšš©š„šØšš: `{convert(result['upload'])}Mb/s`\nšš¢š§š : `{result['ping']}`"
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
*ā ļø Notice:*
*(For Devs Only)*
ā /speedtest *:* Runs a speedtest and check the server speed.
"""

__mod_name__ = "Speedtestā"
__command_list__ = ["speedtest"]
__handlers__ = [SPEED_TEST_HANDLER, SPEED_TEST_CALLBACKHANDLER]
