import requests
res = requests.get("http://google.com") # http://lab.tistory.com"
res.raise_for_status() # google => 정상출력 # tistory => 에러


print("rescode : ", res.status_code) # 200 : 정상 # 400~ : 에러


if res.status_code == requests.codes.ok: # == 200
    print("정상")
else:
    print("문제가 발생했습니다. [에러코드 ", res.status_code, "]")


with open("myscrap.html", "w", encoding="utf8") as f:
    f.write(res.text)