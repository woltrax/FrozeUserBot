
OWNER_TEXT = '''
🤖Ben UserBot kurucusu Woltrax. 2019 yılından beri telegramdayım ve yazılım işleriyle uğraşıyorum.
'''

@bot.on(events.NewMessage(pattern='/kurucu'))
async def owner_cmd(event):
    await event.reply(OWNER_TEXT)
