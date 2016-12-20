#!/usr/bin/python
#-*- coding: UTF-8 -*-
import re
import requests
import yagmail
from bs4 import BeautifulSoup


user = 'wangzhongaochen@163.com'
password = 'wangxinyang+1=?'

raw_data = requests.get('http://music.163.com/discover/toplist?id=64016')
soup = BeautifulSoup(raw_data.content)
t = soup.findAll('ul')[2]
items = t.findAll('li')

# get song info
ind = []; text = []; href = []
for index, item in enumerate(items, 1):
    links = item.findAll('a')[0]
    ind.append(index)
    text.append(links.text[:])
    href.append("http://music.163.com{0}".format(links.attrs.get('href', None)))

# get artists
textarea = [ items.strip(':,') for items in soup.findAll('textarea')[0].text.split('"artists"') ]
artists = [ item for items in textarea for item in items.split(',"alias"') if '"name":' in item and '"}]' in item ]
artist = [','.join(re.findall(r'"name":"(.*?)"}', artist)) for artist in artists ]

content = """ <html> <body> <table> """
for index, text, href, artist in zip(ind, text, href, artist):
    item = "<tr><td>{0}</td><td><a href = '{1}'>{2}</a></td><td> 歌手:{3}</td></tr>".format(index, href, text.encode('utf-8'), artist.encode('utf-8'))
    content += item
content += """ </table> </body> </html> """

with yagmail.SMTP(user=user, password=password, host='smtp.163.com', port=25, smtp_starttls=False) as yag:
    yag.send('wangzhongaochen@163.com', "中国TOP排行榜（内地榜）", content)

