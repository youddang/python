import requests
from bs4 import BeautifulSoup

web = requests.get("https://www.naver.com/").text
soup = BeautifulSoup(web, "html.parser")
keys = soup.select("") #" " 안에 나열하고 싶은 문자열 입력
index = 0

for key in keys:
    index += 1
    print(str(index) + "." + key.text)
    if index >= 20:
        break


print(soup.p)