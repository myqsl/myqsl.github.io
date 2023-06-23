from api_keys import bot_api_key as KEY
from git import Repo
from html import escape
from pathlib import Path
from re import sub
from telegram import Update
from telegram.ext import ApplicationBuilder, filters, MessageHandler, ContextTypes

async def forwarder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post
    if msg:
        # print(msg, flush=True)
        # print(msg.text, flush=True)
        # print(msg.date.ctime() + " " + msg.text, flush=True)
        text = escape(msg.text)
        text = sub(r'(https://youtu.be/[0-9a-zA-Z/]*)', r'<a href="\1">\1</a>', text) 
        line = f'<p><code>{msg.date.strftime("%B %d")}</code>&nbsp;{text}</p>'

        feed = Path('feed.txt')
        lines = feed.read_text().splitlines()
        lines.insert(0, line)
        feed.write_text('\n'.join(lines))

        html = Path('../_includes/updates.html')
        html.write_text('\n'.join(lines[:5]))

        # TODO git pull, add, merge, push
        repo = Repo('..')
        repo.remotes.origin.pull()
        repo.index.add(['.'])

application = ApplicationBuilder().token(KEY).build()
forwardHandler = MessageHandler(filters.TEXT & (~filters.COMMAND), forwarder)
application.add_handler(forwardHandler)
application.run_polling()
