# GET : 누구나 볼 수 있도록 url에 적어 보내는 방식. 보낼 수 있는 데이터의 양이 제한됨.
# POST : URL이 아닌 HTTP 메시지 BODY에 숨겨 보내는 비교적 안전한 방식. 

import requests
import re
from bs4 import BeautifulSoup
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}

for i in range(1, 6):
    print("페이지 :", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)

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

        # ⚠애플 제품 제외하기 
        name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
        if "Apple" in name:
            print("  ⚠Apple 제품은 제외합니다")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        
        # 리뷰 100개 이상, 평점 4.5 이상만 조회
        rating = item.find("em", attrs={"class":"rating"})
        if rating: 
            rating = rating.get_text()
        else:
            rating = "No rated"
            print("  ⚠평점이 없는 상품은 제외합니다")
            continue

        rating_cnt = item.find("span", attrs={"class":"rating-total-count"})
        if rating_cnt: 
            rating_cnt = rating_cnt.get_text()[1:-1] # ex. (56) -> 56
            # print("리뷰 수", rating_cnt)
        else:
            rating_cnt = "No rating Count"
            print("  ⚠평점 수가 없는 상품은 제외합니다")
            continue
        
        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rating) >= 4.5 and int(rating_cnt) >= 100:
            print(f"제품명 : 🐋{name}")
            print(f"가격   : {price}")
            print(f"평점   : ⭐ {rating}점 ({rating_cnt})")
            print("링크   : {}".format("https://www.coupang.com" + link))
            print("-"*100)
        
    
    
    