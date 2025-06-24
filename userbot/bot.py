from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv("config.env")

api_id = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")

bot = TelegramClient('userbot', api_id, api_hash)

import glob
for file in glob.glob("plugins/*.py"):
    exec(open(file, encoding="utf-8").read())

print("Froze UserBot çalışıyor.")
bot.start()
bot.run_until_disconnected()