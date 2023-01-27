import os

"""
Things to be noted you can fill values between empty "" 
Example - JOIN_LOGGER = os.environ.get("EVENT_LOGS", "-100828822882")

• If value is none there add "" to fill if you don't wanna fill add None

• Some vars are already filled to help you no need to change them.
"""


# Token from botfather 
TOKEN = os.environ.get("TOKEN", "5117885347:AAGCl4dYG4tW256fYIXOH2ny2emT-ELjutg")

# Make a new group then add @ScenarioXbot then send /id and fill id here.
JOIN_LOGGER = os.environ.get("EVENT_LOGS", "-1001627401088")

# only one # don't remove other one.
OWNER_ID = int(os.environ.get("OWNER_ID", "1407312928", "fill_your_id_here_")) 

# only one # don't remove other one.
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "sakku_cute", "Your_username_here")

# can add multiple with spaces
DRAGONS = {int(x) for x in os.environ.get("DRAGONS", "1407312928").split()}

# can add multiple with spaces
DEV_USERS = {int(x) for x in os.environ.get("DEV_USERS", "1407312928").split()}

# can add multiple with spaces
DEMONS = {int(x) for x in os.environ.get("DEMONS", "1407312928").split()} 

# can add multiple with spaces
WOLVES = {int(x) for x in os.environ.get("WOLVES", "1407312928").split()}

# can add multiple with spaces
TIGERS = {int(x) for x in os.environ.get("TIGERS", "1407312928").split()}

# Should I show profile pic of user in /info command? 
# default value is true
INFOPIC = bool(os.environ.get("INFOPIC", True)) or "https://telegra.ph/file/a9ec99487ecd550460309.jpg"

# Make a new group then add @ScenarioXbot then send /id and fill id here.
EVENT_LOGS = os.environ.get("EVENT_LOGS", "-1001627401088")

# Don't touch if you don't know.
WEBHOOK = bool(os.environ.get("WEBHOOK", False))

# heroku app url
URL = os.environ.get("URL", "") 
PORT = int(os.environ.get("PORT", 8443))

CERT_PATH = os.environ.get("CERT_PATH")

# Bot Owner's API_ID (From:- https://my.telegram.org/apps)
API_ID = os.environ.get("API_ID", "2879323")

# Bot Owner's API_HASH (From:- https://my.telegram.org/apps)
API_HASH = os.environ.get("API_HASH", "b9a99eb2ab21f20f6b2c792de80f4901")

# Any SQL Database Link (RECOMMENDED:- PostgreSQL & https://www.elephantsql.com)
DB_URI = os.environ.get("DATABASE_URL", "postgres://umjxruwsdnjvax:0cf8c88b1c28e54eb45fe7239aca0a2349a6da479f35a6cb0826bfab5121615a@ec2-23-20-140-229.compute-1.amazonaws.com:5432/descjr9vvh2ruh") 

# Don't touch
DB_URI = DB_URI.replace(
"postgres://", "postgresql://", 1
)  # rest of connection code using the connection string `uri`

# Donation Link (ANY)
DONATION_LINK = os.environ.get("https://t.me/sakku_cute")

# Wall api key for wallpapers # From:- https://wall.alphacoders.com/api.php
WALL_API = os.environ.get("WALL_API", None) 

# To remove background of images # From:- https://www.remove.bg/
REM_BG_API_KEY = os.environ.get("REM_BG_API_KEY", "wnNnNwXYUfnGg5XnJGJ3T2Rz")

## More info written at right side from this line.

OPENWEATHERMAP_ID = os.environ.get("OPENWEATHERMAP_ID", "") # From:- https://openweathermap.org/api
GENIUS_API_TOKEN = os.environ.get("GENIUS_API_TOKEN", None) # From:- http://genius.com/api-clients
MONGO_DB_URI = os.environ.get("MONGO_DB_URI", "mongodb+srv://sakshi:deep9862@cluster0.duuh6.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI", "postgres://ffdqfbhb:x5hzVPg0VpZ2knaBt53X7hRBQDBTauFA@castor.db.elephantsql.com/ffdqfbhb")
SUPPORT_CHAT = os.environ.get("SUPPORT_CHAT", "Aliza_Support") 
SPAMWATCH_SUPPORT_CHAT = os.environ.get("SPAMWATCH_SUPPORT_CHAT", None) # Use @SpamWatchSupport
SPAMWATCH_API = os.environ.get("SPAMWATCH_API", None) # From https://t.me/SpamWatchBot 
BOT_USERNAME = os.environ.get("BOT_USERNAME", "@MissAliza_Bot")


APP_ID = API_ID
APP_HASH = API_HASH
ALLOW_CHATS = os.environ.get("ALLOW_CHATS", True) # Don't Change
BOT_NAME = os.environ.get("BOT_NAME", True)
ARQ_API_URL = "https://arq.hamker.in"
GOOGLE_CHROME_BIN = "/usr/bin/google-chrome"
CHROME_DRIVER = "/usr/bin/chromedriver"


BL_CHATS = {int(x) for x in os.environ.get("BL_CHATS", "").split()}


# Don't Change
LOAD = os.environ.get("LOAD", "").split() 

# Don't Change
NO_LOAD = os.environ.get("NO_LOAD", "rss").split()

# Don't Change
DEL_CMDS = bool(os.environ.get("DEL_CMDS", "True"))

# Don't Change
STRICT_GBAN = bool(os.environ.get("STRICT_GBAN", False)) or "True"

# Don't Change
WORKERS = int(os.environ.get("WORKERS", 8))

# Sticker id here if you want to ban any
BAN_STICKER = os.environ.get("BAN_STICKER", "CAACAgUAAxkBAAEDafNhq5Z0DegqVzauwSighMw5cPWp8QACVgQAAuUG0FRXfCEuBziNzCIE")

# Don't Change
ALLOW_EXCL = os.environ.get("ALLOW_EXCL", False)

# Don't Change
TEMP_DOWNLOAD_DIRECTORY = os.environ.get("TEMP_DOWNLOAD_DIRECTORY", "./")

# Already filled no need to fill again.
CASH_API_KEY = os.environ.get("CASH_API_KEY", None) or "PS4Q42YT2D2VFVMQ"

# Already filled no need to fill again.
TIME_API_KEY = os.environ.get("TIME_API_KEY", None) or "RPWFECCNJHH6"
