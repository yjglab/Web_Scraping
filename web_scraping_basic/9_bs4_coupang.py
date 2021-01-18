# GET : 누구나 볼 수 있도록 url에 적어 보내는 방식. 보낼 수 있는 데이터의 양이 제한됨.
# POST : URL이 아닌 HTTP 메시지 BODY에 숨겨 보내는 비교적 안전한 방식. 

import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("li", attrs={"class":re.compile("^search-product")}) # class명이 search-product로 시작하는 것과 일치하는 모든 li태그
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items: # 모든 노트북 상품 정보 가져오기

    # ⚠광고 상품 제외하기 
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print("  ⚠광고 상품은 제외합니다")
        continue
    
    name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
    price = item.find("strong", attrs={"class":"price-value"}).get_text()
    rating = item.find("em", attrs={"class":"rating"})
    if rating: 
        rating = rating.get_text()
    else:
        rating = "||No rated||"
    rating_cnt = item.find("span", attrs={"class":"rating-total-count"})
    if rating_cnt: 
            rating_cnt = rating_cnt.get_text()
    else:
            rating_cnt = "||No rating Count||"
    print(name, price, rating, rating_cnt)
    print()
    