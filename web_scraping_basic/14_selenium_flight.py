from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome("./chromedriver.exe")
browser.maximize_window() # 창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url)

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()
# 이번달 27일, 28일 선택
browser.find_elements_by_link_text("27")[1].click() # 이번 달
browser.find_elements_by_link_text("28")[1].click() # 다음 달
# 제주 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()
# 항공권 검색 버튼 클릭
browser.find_element_by_link_text("항공권 검색").click()
# 대기 (10s 이후에도 나오지 않으면 에러)
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[1]"))) # By.XPATH 외 다른 값도 가능
    print(elem.text)
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
# print(elem.text)