from bot import bot
from telethon import events

HELP_TEXT = '''
🤖 Froze UserBot için Kullanılabilir Komutlar:

/ping - Botun tepki verip vermediğini kontrol eder
/alive - Botun çalışıp çalışmadığını gösterir
/help - Bu yardım mesajını gösterir
/afk - AFK modunu açar
/restart - Botu yeniden başlatır (gelişmiş kullanımda çalışır)
/calc - Matematik işlemi yapar
/coin - Yazı Tura atar
/id - Kullanıcının İdsini atar
/rate - Botun bir şey için 100 üzerinden puan verir
/otoguncelle - İsminin sonuna son aktif olma saatini yazar
/afk - Afk iken size yazan kişiye otomatik mesaj atar
/afk mesaj - mesaj yerine girdiğiniz metin afk iken atılacak mesajı değiştirir
/back - afk modunu kapatıp sana yazanları gösterir
/time zamanı söyler

'''

@bot.on(events.NewMessage(pattern='/help'))
async def help_cmd(event):
    await event.reply(HELP_TEXT)
