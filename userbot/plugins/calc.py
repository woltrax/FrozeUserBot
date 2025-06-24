from bot import bot
from telethon import events

@bot.on(events.NewMessage(pattern='/calc (.*)'))
async def calc(event):
    try:
        expression = event.pattern_match.group(1)
        result = eval(expression)
        await event.reply(f"🧮 Sonuç: {result}")
    except Exception as e:
        await event.reply(f"❌ Hata: {str(e)}")