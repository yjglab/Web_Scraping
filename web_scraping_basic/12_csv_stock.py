import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf8", newline="") # 한글 깨질 시, utf-8-sig
writer = csv.writer(f) # writer를 활용하여 파일 작성

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE".split("\t") # ["N", "종목명", ... ]
print(title)
writer.writerow(title)

for page in range(1, 5):
    res = requests.get(url + str(page))
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")
    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")
    
    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: # 무의미한 줄 바꿈 용 데이터 skip
            continue
        data = [column.get_text().strip() for column in columns] # strip() : 불필요한 공백 제거용
        
        writer.writerow(data) # writerow() 넣을 시 list 형태로 값을 넣어주어야 함.