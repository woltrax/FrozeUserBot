from bot import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/ping'))
async def ping(event):
    await event.reply("Pong! 🏓")