import datetime
from bot import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/time'))
async def show_time(event):
    now = datetime.datetime.now()
    await event.reply(f"🕒 Şu anki zaman: {now.strftime('%Y-%m-%d %H:%M:%S')}")