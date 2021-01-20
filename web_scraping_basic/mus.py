import time
from selenium import webdriver

browser = webdriver.Chrome("./chromedriver.exe") 
browser.get("https://store.musinsa.com/app/?NaPm=ct%3Dkk43y13y%7Cci%3Dcheckout%7Ctr%3Dds%7Ctrx%3D%7Chk%3Ded98f7f51ae5131ded5db7fac4eeb3251737d69e")

elem = browser.find_element_by_xpath("//*[@id='default_top']/div[3]/ul/li[1]/a")
elem.click()

browser.find_element_by_name("id").send_keys("")
browser.find_element_by_name("pw").send_keys("")
browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/form/span[3]/input").click()

time.sleep(1)
browser.find_element_by_xpath("//*[@id='ranking_goods_pager']/li[19]/a").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='ranking_goods']/div[19]/ul/li[1]/div[1]/a/img").click()

browser.find_element_by_class_name("btn_black").click()
time.sleep(1)
browser.find_element_by_xpath("//*[@id='payment_info_area']/ul[5]/li[1]/label/span").click()

browser.find_element_by_id("btn_pay").click()