from bot import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/alive'))
async def alive(event):
    await event.reply("✅ Bot çalışıyor!")