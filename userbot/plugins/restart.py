import os
import sys
from bot import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/restart'))
async def restart_bot(event):
    await event.reply("♻️ Yeniden başlatılıyor...")
    os.execl(sys.executable, sys.executable, *sys.argv)