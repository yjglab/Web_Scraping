### headless 크롬으로 user-agent 정보 사용 시 options에서 미리 설정 필요

from selenium import webdriver

# 크롬을 백그라운드에서 작동하기
options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080") # 내부적으로 fhd 크기로 작동
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36")
# headless 크롬으로 접근 시 user-agent 정보 접근을 방지하므로 미리 설정

browser = webdriver.Chrome(options=options) # 옵션 적용
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

browser.quit()

# Python selenium 도움 문서
# https://selenium-python.readthedocs.io/