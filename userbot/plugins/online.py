from bot import bot
from telethon import events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import UserStatusOffline, UserStatusOnline
import asyncio
import datetime

default_name = None

async def check_status_loop():
    global default_name
    while True:
        try:
            me = await bot.get_me()
            full = await bot(GetFullUserRequest(me.id))
            status = full.user.status

            if default_name is None:
                default_name = me.first_name

            if isinstance(status, UserStatusOffline):
                dt = status.was_online.replace(tzinfo=None)
                saat = dt.strftime('%H:%M')
                new_name = f"{default_name} (⏳: {saat})"
                if me.first_name != new_name:
                    await bot(UpdateProfileRequest(first_name=new_name))
            elif isinstance(status, UserStatusOnline):
                if me.first_name != default_name:
                    await bot(UpdateProfileRequest(first_name=default_name))
        except Exception as e:
            print(f"Hata: {e}")
        await asyncio.sleep(60)

@bot.on(events.NewMessage(pattern='/otoguncelle'))
async def manual_start(event):
    await event.reply("⏳ Otomatik isim güncelleyici başlatıldı.")
    await check_status_loop()