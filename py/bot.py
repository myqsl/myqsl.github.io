from api_keys import bot_api_key as KEY
from git import Repo
from html import escape
from pathlib import Path
from re import sub
from telegram import Update
from telegram.ext import ApplicationBuilder, filters, MessageHandler, ContextTypes

async def forwarder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post
    if not msg: return
    
    text = escape(msg.text)
    text = sub(r'([a-z]*://[0-9a-zA-Z/_]*)', r'<a href="\1">\1</a>', text)
    text = sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = sub(r'__(.*?)__', r'<em>\1</em>', text)
    line = f'<p><code>{msg.date.strftime("%B %d")}</code>&nbsp;{text}</p>'

    feed = Path('feed.txt')
    lines = feed.read_text().splitlines()
    lines.insert(0, line)
    feed.write_text('\n'.join(lines))

    html = Path('../_includes/updates.html')
    html.write_text('\n'.join(lines[:5]))

    repo = Repo('..')
    repo.remotes.origin.pull()
    repo.index.add(['py/feed.txt', '_includes/updates.html'])
    repo.index.commit("myqsl_github_io: updates were added.")
    repo.remotes.origin.push()


application = ApplicationBuilder().token(KEY).build()
forwardHandler = MessageHandler(filters.TEXT & (~filters.COMMAND), forwarder)
application.add_handler(forwardHandler)
application.run_polling()
