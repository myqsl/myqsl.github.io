from os import scandir, listdir
from os.path import splitext
from re import fullmatch
from subprocess import run
from sys import stderr
from typing import Any

def print_attr(obj: dict[str, Any], attr: str, /, optional: bool=False) -> str:
    if attr not in obj:
        assert optional
        return f'# {attr}: '
    else:
        return f'{attr}: {obj[attr]}'

def read_orig_post(path: str) -> dict[str, Any]:
    m = fullmatch(r'_posts_old/(.+)\.md', path)
    assert m
    code = m[1]

    with open(path, 'r') as f:
        in_meta = False
        in_gallery = False
        orig_post = dict[str, Any]()
        orig_post['code'] = code
        content = list[str]()
        orig_post['content'] = content
        gallery = list[str]()
        orig_post['gallery'] = gallery

        for line in f.readlines():
            line = line.strip()
            if line == '---':
                in_meta = not in_meta
                in_gallery = False
            elif line == 'gallery:':
                in_gallery = True
            elif line.startswith('#'): # comment
                pass
            elif not in_meta:
                content.append(line)
            elif in_gallery:
                m = fullmatch(r'- (.+)', line)
                assert m
                gallery.append(m[1])
            else:
                m = fullmatch(r'([A-Za-z_]+): (.+)', line)
                assert m
                attr = m[1]
                value = m[2]
                assert attr not in orig_post
                orig_post[attr] = value

        return orig_post

def write_new_post(new_post: dict[str, Any]):
    assert f"{new_post['code']}.md" not in listdir('_posts')
    nl = '\n'
    with open(f"_posts/{new_post['code']}.md", 'w') as f:
        f.write(f"""---
{print_attr(new_post, 'title')}
{print_attr(new_post, 'kind')}
{print_attr(new_post, 'mail_to', optional=True)}
{print_attr(new_post, 'report_sent', optional=True)}
{print_attr(new_post, 'responce_sent', optional=True)}
{print_attr(new_post, 'responce_received')}
{print_attr(new_post, 'serie')}
receptions:
{nl.join('  - ' + render_reception(r) for r in new_post['receptions'])}
gallery:
{nl.join('  - ' + line for line in new_post['gallery'])}
---
{nl.join(new_post['content'])}""")


def render_reception(reception: dict[str, str]):
    return f"""{print_attr(reception, 'frequency')}
    {print_attr(reception, 'language')}
    {print_attr(reception, 'date')}
    {print_attr(reception, 'time')}
    {print_attr(reception, 'location')}
    {print_attr(reception, 'receiver', optional=True)}
    {print_attr(reception, 'antenna', optional=True)}
    {print_attr(reception, 'station', optional=True)}
    {print_attr(reception, 'youtube_id', optional=True)}
"""


def reformat_orig_post(orig_post: dict[str, Any]):
    new_post = dict[str, Any]()
    new_post['code'] = orig_post['code']
    new_post['title'] = orig_post['title']
    new_post['kind'] = orig_post['kind']
    if 'mail_to' in orig_post:
        new_post['mail_to'] = orig_post['mail_to']
    if 'report_sent' in orig_post:
        new_post['report_sent'] = orig_post['report_sent']    
    if 'responce_sent' in orig_post:
        new_post['responce_sent'] = orig_post['responce_sent']
    new_post['responce_received'] = orig_post['responce_received']
    new_post['serie'] = orig_post['serie']
    new_post['gallery'] = orig_post['gallery']
    new_post['content'] = orig_post['content']
    new_post['receptions'] = list[dict[str, str]]()

    if 'frequency' not in orig_post:
        assert 'language' not in orig_post
        assert 'reception_time' not in orig_post
        assert 'reception_date' not in orig_post
        assert 'location' not in orig_post
        assert 'receiver' not in orig_post
        assert 'antenna' not in orig_post
        assert 'station' not in orig_post
        assert 'youtube_id' not in orig_post
    else:
        with_kHz = False
        freqs_kHz = orig_post['frequency'].split(' kHz')
        assert len(freqs_kHz) in {1, 2}
        with_kHz = (len(freqs_kHz) == 2)
        freqs = freqs_kHz[0].split('/')
        assert orig_post['language']
        langs = orig_post['language'].split('/')
        assert len(langs) in {1, len(freqs)}
        times = orig_post['reception_time'].split('/')
        assert len(times) in {1, len(freqs)}
        for i, freq in enumerate(freqs):
            assert ' ' not in freq

            reception = dict[str, str]()
            new_post['receptions'].append(reception)

            reception['frequency'] = freq + (' kHz' if with_kHz else '')
            reception['language'] = langs[0 if len(langs) == 1 else i]
            assert '/' not in orig_post['reception_date']
            reception['date'] = orig_post['reception_date']
            reception['time'] = times[0 if len(times) == 1 else i]
            if len(freqs) > 1 and len(times) == 1:
                print(f'Fix time for reception[{i}] in', new_post['code'])
            assert '/' not in orig_post['location']
            reception['location'] = orig_post['location']
            if 'receiver' in orig_post:
                assert '/' not in orig_post['receiver']
                reception['receiver'] = orig_post['receiver']
            if 'antenna' in orig_post:
                assert '/' not in orig_post['antenna']
                reception['antenna'] = orig_post['antenna']
            if 'station' in orig_post:
                assert '/' not in orig_post['station']
                reception['station'] = orig_post['station']
            if 'youtube_id' in orig_post:
                assert '/' not in orig_post['youtube_id']
                reception['youtube_id'] = orig_post['youtube_id']

    return new_post


run("rm -rf _posts/*", shell=True, check=True)

for f in scandir('_posts_old'):

    if splitext(f.path)[1] != '.md':
        print('Not a directory, skipped:', f.path, file=stderr)
        continue

    orig_post = read_orig_post(f.path)
    new_post = reformat_orig_post(orig_post)
    write_new_post(new_post)
# TODO search for doubles of receptions
