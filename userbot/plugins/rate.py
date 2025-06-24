import random
from bot import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/rate (.*)'))
async def rate(event):
    item = event.pattern_match.group(1)
    rating = random.randint(1, 100)
    await event.reply(f"💡 {item} için puanım: {rating}/100")