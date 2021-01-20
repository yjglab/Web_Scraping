# 1. pip install selenium
# 2. 웹드라이버 (中 크롬 드라이버 - 크롬 버전 확인 후) 설치

import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe") # 크롬 webdriver 객체 생성. # webdriver.exe 가 다른 경로에 있을 경우 해당 경로를 입력

# 1. 브라우저 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw 입력 (잘못된 값 입력)
browser.find_element_by_id("id").send_keys("fault") 
browser.find_element_by_id("pw").send_keys("fault")

# 4, login 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(2)

# 5. id 를 새로 입력
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("mynewid")

# 6. html 정보 출력
print(browser.page_source) # 현재 페이지의 모든 html문서 출력

# 7. 브라우저 종료
browser.close() # 현재 탭만 종료
browser.quit()

# 변수.find_element_by_name("text") : name이 text인 태그의 정보 저장
# 변수.find_element_by_xpath("경로") : xpath 정보 저장 (경로 찾기 : 저장 하려는 태그에 우클릭 - copy - xpath)
# 변수.find_element_by_class_name("클래스명")
# 변수.find_element_by_id("id명")
# 변수.click() : 해당 요소 클릭
# 변수.back() : 해당 브라우저 뒤로가기
# 변수.forward() : 해당 브라우저 앞으로가기
# 변수.refresh() : 새로고침
# from selenium.webdriver.common.keys import Keys : 키입력 관련 import
# 변수.send_keys("aa") : 변수에 "aa" 전송
# 변수.send_keys(Keys.ENTER) : 변수 ENTER 클릭
# 변수.browser.quit()