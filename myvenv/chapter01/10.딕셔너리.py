# 딕셔너리
# : 사전형태의 자료형

stock_a = {"삼성전자" : 82000, "LG전자" : 150000}

stock_b = {
    "삼성전자" : [81000, 81500, 82000, 81500, 82000],
    "LG전자" : (150000, 149000, 148000, 151000, 152000)
}

# 중첩 딕셔너리
stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 5,
        "매수단가" : 81000
    }
}

# alt + shift 하면 위 아래로 복사됩니다.
print(stock_a)
print(stock_b)
print(stock_c)

# 딕셔너리 접근하기
print(stock_a["삼성전자"])  # 82000
print(stock_c["삼성전자"]["보유수량"])  # 5

# 딕셔너리 할당하기
stock_a["삼성전자"] = 85000
print(stock_a) 

# 딕셔너리 삭제하기
del stock_a["LG전자"]
print(stock_a)

# 딕셔너리 함수
stock_d = {
    "삼성전자" : 82000,
    "LG전자" : 123000,
    "카카오" : 170000,
    "NAVER" : 370000
}

# items()
print(stock_d.items())

for item in stock_d.items():
    # 튜플형태로 들어가 있습니다.
    print(item)
    # 키만 출력하고 싶을때
    print(item[0])
    # 아이템만 출력하고 싶을때
    print(item[1])

# keys() : 키만 출력
for key in stock_d.keys():
    print(key)

# values() : 데이터들만 출력
for value in stock_d.values():
    print(value)