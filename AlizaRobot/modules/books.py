import os
import re

import requests
from bs4 import BeautifulSoup
from telethon import events

from AlizaRobot import BOT_USERNAME, SUPPORT_CHAT, telethn


@telethn.on(events.NewMessage(pattern="^/book (.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    KkK = await event.reply("Searching for the book...")
    lin = "https://b-ok.cc/s/"
    text = input_str
    link = lin + text

    headers = [
        "User-Agent",
        "Arsh 5.0 (Macintosh; Intel Mac OS X 10.15; rv:74.0) Gecko/20100101 Firefox/74.0",
    ]
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    f = open("book.txt", "w")
    total = soup.find(class_="totalCounter")
    for nb in total.descendants:
        nbx = nb.replace("(", "").replace(")", "")
    if nbx == "0":
        await event.reply("No Books found with that name.")
    else:

        lool = 0
        for tr in soup.find_all("td"):
            for td in tr.find_all("h3"):
                for ts in td.find_all("a"):
                    title = ts.get_text()
                    lool += 1
                for ts in td.find_all("a", attrs={"href": re.compile("^/book/")}):
                    ref = ts.get("href")
                    link = f"https://b-ok.cc{ref}"

                f.write("\n" + title)
                f.write("\nBook Link:- " + link + "\n\n")

        f.write(f"ʙʏ @{BOT_USERNAME}.")
        f.close()
        caption = f"AlizaRobot  \nJoin Support @{SUPPORT_CHAT} "

        await telethn.send_file(
            event.chat_id,
            "book.txt",
            caption=f"**BOOKS GATHERED SUCCESSFULLY!\n\nBY @AlizaRobot **",
        )
        os.remove("book.txt")
        await KkK.delete()
