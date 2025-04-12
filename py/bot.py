from api_keys import bot_api_key as KEY
from git import Repo
from html import escape
from pathlib import Path
from telegram import Update
from telegram.constants import MessageEntityType
from telegram.ext import ApplicationBuilder, filters, MessageHandler, ContextTypes

def splitted(text, entities):
    ln = 0
    for e in entities:
        yield (text[ln:e.offset], None)
        yield (text[e.offset:e.offset + e.length], e.type)
        ln = e.offset + e.length
    yield (text[ln:], None)

def is_youtube(url):
    youtube_domains = [
        'https://www.youtube.com/',
        'http://www.youtube.com/',
        'https://m.youtube.com/',
        'http://m.youtube.com/',
        'https://youtu.be/',
        'http://youtu.be/',
        'https://m.youtu.be/',
        'http://m.youtu.be/',
    ]
    return any(d for d in youtube_domains if url.startswith(d))

def is_this_site(url):
    this_domains = [
        'https://myqsl.github.io/',
        'http://myqsl.github.io/',
    ]
    return any(d for d in this_domains if url.startswith(d))

def html_text(text, entity_type):
    if not entity_type:
        return escape(text)
    elif entity_type == MessageEntityType.URL:

        url = text
        if text.startswith('https://myqsl.github.io/'):
            url = text[len('https://myqsl.github.io'):]
        elif text.startswith('http://myqsl.github.io/'):
            url = text[len('http://myqsl.github.io'):]

        link_text = escape(text)
        if is_youtube(text):
            link_text = f'<img src="/assets/images/yt.png"/>'
        elif is_this_site(text):
            link_text = f'<img src="/assets/images/share.png"/>'

        return f'<a href="{url}">{link_text}</a>'

    elif entity_type == MessageEntityType.EMAIL:
        return f'<a href="mailto:{text}"><img src="/assets/images/mail.png"/></a>'
    elif entity_type == MessageEntityType.BOLD:
        return f'<strong>{escape(text)}</strong>'
    elif entity_type == MessageEntityType.ITALIC:
        return f'<emph>{escape(text)}</emph>'
    elif entity_type == MessageEntityType.UNDERLINE:
        return f'<u>{escape(text)}</u>'
    elif entity_type == MessageEntityType.STRIKETHROUGH:
        return f'<s>{escape(text)}</s>'
    elif entity_type == MessageEntityType.PRE:
        return f'<pre>{escape(text)}</pre>'
    elif entity_type == MessageEntityType.CODE:
        return f'<code>{escape(text)}</code>'
    else:
        return escape(text)

async def forwarder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.channel_post
    if not msg: return

    line = ''
    for text, entity_type in splitted(msg.text, msg.entities):
        line += html_text(text, entity_type)
    line = f'<p><code>{msg.date.strftime("%B %d")}</code>&nbsp;{line}</p>'

    feed = Path('feed.txt')
    lines = feed.read_text(encoding='utf-16-le').splitlines()
    lines.insert(0, line)
    feed.write_text('\n'.join(lines), encoding='utf-16-le')

    html = Path('../_includes/updates.html')
    html.write_bytes('\n'.join(lines[:5]).encode('utf-8'))

    repo = Repo('..')
    repo.remotes.origin.pull()
    repo.index.add(['py/feed.txt', '_includes/updates.html'])
    repo.index.commit("myqsl_github_io: updates were added.")
    repo.remotes.origin.push()

print('Myqsl bot is temporaray disabled, sorry')
if False:
    application = ApplicationBuilder().token(KEY).build()
    forwardHandler = MessageHandler(filters.TEXT & (~filters.COMMAND), forwarder)
    application.add_handler(forwardHandler)
    application.run_polling()
