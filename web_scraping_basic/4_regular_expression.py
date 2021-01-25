import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave
# caae, cabe, cace, cade, ...

# 정규식 사용하기
    # . => 하나의 문자    (ca.e) ex. care, cafe, case (o) | caffe (x)
    # ^ => 문자열의 시작  (^de) ex. desk, destination (o) | fase (x)
    # $ => 문자열의 끝    (se$) ex. case, base (o) | face (x)
p = re.compile("ca.e") 

def print_match(m):
    if m: # 매치되었다면
        print("m.group() : ", m.group()) # 일치하는 문자열을 반환
        print("m.string : ", m.string) # 입력받은 문자열을 반환
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 index 반환
        print("m.end() : ", m.end()) # 일치하는 문자열의 끝 index 반환
        print("m.span(): ", m.span()) # 일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음.")    

# match() : 주어진 문자열의 처음부터 일치하는 지 확인
m = p.match("case")
print_match(m) # case => 정규식 p와 매치되어 출력됨. 매치되지 않으면 에러.
print()
m = p.match("good care")
print_match(m) # 매칭되지 않음.
print()
m = p.match("careless") 
print_match(m) # care
print()

# search() : 주어진 문자열 중에 일치하는 게 있는 지 확인
m = p.search("good care") 
print_match(m) # care

# findall() : 일치하는 모든 것을 list 로 반환
lst = p.findall("careless") 
print(lst) # ['care']
lst = p.findall("good care cafe") 
print(lst) # ['care', 'cafe']


# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는 지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는 게 있는 지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 list 로 반환

