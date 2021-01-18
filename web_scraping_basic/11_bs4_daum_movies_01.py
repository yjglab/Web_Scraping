import requests
from bs4 import BeautifulSoup



for year in range(2015, 2020):
    url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
    res = requests.get(url)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class":"thumb_img"})

    for idx, image in enumerate(images):
        # print(image["src"])
        image_url = image["src"]
        if image_url.startswith("//"): 
            image_url = "https:" + image_url
            
        print(image_url)

        # 이미지 링크에 들어가서 파일 저장하기
        image_res = requests.get(image_url)
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year, idx + 1), "wb") as f:
            f.write(image_res.content) # resource 가 가지고 있는 content 정보 (== 이미지)
            
        if idx >= 4:
            break