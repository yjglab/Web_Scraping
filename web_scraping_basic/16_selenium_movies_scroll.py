
from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://play.google.com/store/movies/top"
browser.get(url)

# 스크롤 내리기 ( js 코드 즉시 실행 )
# browser.execute_script("window.scrollTo(0, 1080)") # 화면 (가로, 세로) # (0, 1080) 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") # 화면 세로 끝까지 스크롤 내리기

browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import time 
interval = 2 # 2초에 한번씩 스크롤 내림
prev_height = browser.execute_script("return document.body.scrollHeight") # 현재 문서 높이 가져오기

while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    
    prev_height = curr_height

print("스크롤 완료")


import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"}) # class 명 2개 찾기 : {"class":["class1", "class2"]}
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title) # 스크롤 끝 까지 내린 모든 영화 제목

    # 할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, "😕 할인되지 않은 영화 제외")
        continue

    # 할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    
    if "₩" in original_price:
        original_price = original_price[1:]
        price = price[1:]
        
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 150)

browser.quit()