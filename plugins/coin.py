import random
from bot import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/coin'))
async def coin(event):
    result = random.choice(['Yazı', 'Tura'])
    await event.reply(f"🪙 Sonuç: {result}")