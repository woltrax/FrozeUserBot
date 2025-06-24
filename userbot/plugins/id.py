from bot import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/id'))
async def get_id(event):
    sender = await event.get_sender()
    await event.reply(f"👤 Kullanıcı ID: `{sender.id}`")