from bot import bot
from telethon import events

AUTHORIZED_USERS = [123456789]  # Sadece bu ID'ye sahip kullanıcılar komutları kullanabilir

def is_authorized(event):
    return event.sender_id in AUTHORIZED_USERS

@bot.on(events.NewMessage(pattern='/secure'))
async def secure_command(event):
    if is_authorized(event):
        await event.reply("🔐 Yetkilisin!")
    else:
        await event.reply("🚫 Bu komutu kullanamazsın.")