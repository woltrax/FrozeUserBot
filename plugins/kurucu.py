
HELP_TEXT = '''
🤖Ben UserBot kurucusu Woltrax. 2019 yılından beri telegramdayım ve yazılım işleriyle uğraşıyorum.
'''

@bot.on(events.NewMessage(pattern='/kurucu'))
async def help_cmd(event):
    await event.reply(HELP_TEXT)