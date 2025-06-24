from bot import bot
from telethon import events
import time

afk_status = False
afk_message = "🤖 Sahibim şu an aktif değil. \nAktif olunca dönüt verecektir. \nBen FROZE UserBot, sahibimi korumakla görevliyim."
afk_start_time = 0
afk_logs = []
already_replied = set()

@bot.on(events.NewMessage(pattern='/afk(?: (.*))?'))
async def set_afk(event):
    global afk_status, afk_message, afk_start_time, afk_logs, already_replied
    msg = event.pattern_match.group(1)
    afk_status = True
    afk_logs = []
    already_replied.clear()
    afk_start_time = time.time()
    if msg:
        afk_message = msg
        await event.reply(f"🕒 AFK mesajınız ayarlandı:\n{afk_message}")
    else:
        await event.reply("🕒 AFK moduna geçildi. Varsayılan mesaj gönderilecek.")

@bot.on(events.NewMessage(pattern='/back'))
async def remove_afk(event):
    global afk_status, afk_logs
    afk_status = False
    summary = "✅ AFK modu kapatıldı."
    if afk_logs:
        summary += f"\n🧾 {len(afk_logs)} kişi seni yokluğunda aradı:"
        for i, (sender, msg) in enumerate(afk_logs, 1):
            summary += f"\n{i}. {sender}: {msg}"
    else:
        summary += "\nKimse seni aramadı. 🫢"
    afk_logs = []
    await event.reply(summary)

@bot.on(events.NewMessage())
async def auto_afk_reply(event):
    global afk_status, afk_message, afk_start_time, afk_logs, already_replied
    if afk_status and not event.out:
        sender = await event.get_sender()
        sender_id = sender.id

        # Sadece ilk mesajda yanıtla
        if sender_id not in already_replied:
            already_replied.add(sender_id)

            duration = int(time.time() - afk_start_time)
            minutes = duration // 60
            seconds = duration % 60
            since = f"{minutes} dk {seconds} sn önce"

            reply_text = f"{afk_message}\n\n📆 AFK olalı: {since}"
            afk_logs.append((sender.first_name, event.message.message))
            await event.reply(reply_text)