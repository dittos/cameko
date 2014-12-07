import re
import feedparser

url = 'http://www.nyaa.se/?page=rss&cats=1_11&maxsize=600'
trusted_raws = ['Zero-Raws', 'Leopard-Raws', 'Ohys-Raws']

d = feedparser.parse(url)
for entry in d.entries:
    dl_url = entry.link
    title = entry.title
    m = re.match('^\[(?P<raw>.+?)\]\s*(?P<title>.+)\s+-\s+(?P<episode>[0-9]+)(?:\s+RAW)?\s+\((?P<source>.+?)\s+(?P<format>.+)\)\.mp4$', title)
    if not m:
        continue
    raw = m.group('raw')
    if raw not in trusted_raws:
        continue
    print m.group('title')
