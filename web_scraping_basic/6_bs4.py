# pip install beautifulsoup4, lxml
# lxml : 구문 분석 파서

import requests
from bs4 import BeautifulSoup

# 네이버 웹툰

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml") # res.text -> html 문서 / html문서를 lxml파서를 통해 BeautifulSoup 객체로 생성하여 저장
print(soup.title) # <title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
print(soup.title.get_text()) # 네이버 만화 > 요일별  웹툰 > 전체웹툰
print(soup.a) # 첫번째로 발견된 a태그의 정보 출력
print(soup.a.attrs) # 첫번째로 발견된 a태그의 속성값들 출력
print(soup.a["href"]) # #menu  a태그의 특정 속성값을 출력

print()
print(soup.find("a", attrs={"class":"Nbtn_upload"})) # a태그이며 속성이 class이고 class명이 "~"인 정보 출력 # <a class="Nbtn_upload" href="/mypage/myActivity.nhn" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>
print(soup.find(attrs={"class":"Nbtn_upload"})) # 위와 동일(중복이 없는 경우만)

print()
print(soup.find("li", attrs={"class":"rank01"})) # class가 rank01인 li태그와 담긴 정보 출력
rank1 = soup.find("li", attrs={"class":"rank01"})
print(rank1.a)
print(rank1.a.get_text()) 
print()
print(rank1.next_sibling) # 줄바꿈 단계이므로 빈 값을 출력함.
rank2 = rank1.next_sibling.next_sibling # rank2에 대한 li 정보
rank3 = rank2.next_sibling.next_sibling
rank2 = rank2 = rank3.previous_sibling.previous_sibling

rank2 = rank1.find_next_sibling("li") # <-> find_previous_sibling
print(rank2.a.get_text())

# print(rank1.parent) # rank1 li태그의 부모인 ol 태그의 모든 정보 출력

print()
rank1.find_next_siblings("li") # rank1 기준 다음 모든 li형제 태그들 출력

webtoon = soup.find("a", text="독립일기-57화 반려 식물") # text는 <a>와 </a> 사이 text
print(webtoon) # 해당하는 a태그 정보 출력 
