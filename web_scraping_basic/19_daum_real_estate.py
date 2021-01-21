# import requests
# from bs4 import BeautifulSoup

# url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
# res = requests.get(url)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# table = soup.find("table", attrs={"class":"tbl"})

# for i in range(1, 6):
#     tr = table.find_all("tr")    
#     td = tr.find_all("td", attrs={"class":"col" + str(i)})

#     txt = td.find("div", attrs={"class":"txt_ac"}).get_text()

#     print(txt)
    

import requests
from bs4 import BeautifulSoup

url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# with open("daum_real_estate.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

data_rows = soup.find("table", attrs={"class":"tbl"}).find("tbody").find_all("tr")
for idx, row in enumerate(data_rows):
    columns = row.find_all("td")

    print("==========매물 {}==========".format(idx + 1))
    print("거래 :", columns[0].get_text())
    print("면적 :", columns[1].get_text())
    print("가격 :", columns[2].get_text())
    print("동   :", columns[3].get_text())
    print("층   :", columns[4].get_text())
    