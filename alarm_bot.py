from http import client
from multiprocessing.connection import Client
import requests
from bs4 import BeautifulSoup
import time
import discord
import asyncio

token = ''
clt = discord.Client()
url = 'https://www.dongyang.ac.kr/dongyang/129/subview.do'

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

compare_text_1 = soup.find("td", attrs={"class":"td-subject"})

while True:
    compare_text_2 = soup.find("td", attrs={"class":"td-subject"})
    if compare_text_1 == compare_text_2:
        time.sleep(30)
    else:
        @clt.event
        async def on_ready(msg):
            await msg.channel.send("새로운 공지사항이 올라왔습니다! 공지사항 홈페이지를 참고해 주세요.\n", url)
        clt.run(token)
        time.sleep(30)
        break


