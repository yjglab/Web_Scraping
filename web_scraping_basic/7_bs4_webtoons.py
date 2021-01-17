import requests
from bs4 import BeautifulSoup

# 네이버 웹툰

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()


soup = BeautifulSoup(res.text, "lxml")

# 네이버 웹툰 전체 목록
cartoons = soup.find_all("a", attrs={"class":"title"})
for cartoon in cartoons:
    print(cartoon.get_text())