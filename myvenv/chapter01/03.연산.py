# 1. 대입연산
# 변수이름 = 데이터

# 2. 산술연산
# - 숫자연산
x = 4
y = 2

print(x + y)
print(x - y)
print(x / y)
print(x * y)
print(x ** y) # 제곱
print(x // y) # 몫
print(x % y) # 나머지


# - 문자열연산
tag1 = "#내꺼하자"
tag2 = "#오늘부터1일"
tag3= "#Python이랑"

tag = tag1 + tag2 + tag3
print(tag)
# #내꺼하자#오늘부터1일#Python이랑출력

name = "python"
message = "우리 모두 {}을 사랑합니다.\n".format(name) * 3
print(message)
# 우리 모두 python을 사랑합니다.
# 우리 모두 python을 사랑합니다.
# 우리 모두 python을 사랑합니다.
# 출력

# 복합할당연산자
level = 10 
level = level + 1 # 레벨 1 증가
# 위와 동일, level = level + 1
level += 1  # 레벨 1 증가

health = 2000
health -= 300  # 체력 300 감소

attack = 100
attack *= 2 # 공격력 2배 증가

print(level, health, attack)


# 1. 비교연산

print(2 > 3) # False
print(15 < 30) # True
print(3 <= 3) # True
print("kimchi" == "soy")  # False

# 2. 논리연산

print(4 < 6 and 10 >= 10) # True
print("10" == 10) # False
print(not 5 == 5) # False
print('-'*10)
print(not 5) # False
good_list = ['good', 'good2']

if 'good' not in good_list:
    print("good이 안에 없어요!")
else:
    print("good이 안에 있어요!")

# 3. 멤버십연산
print("a" in "abc") # 포함되어 있으니 True
print(good_list[0].startswith('g')) # True

print("d" not in "abc") # True

for i in good_list:
    if i.endswith('2'):
        print(i) # good2
    else:
        pass

a = int(input("숫자를 입력하세요: "))
b = int(input("숫자를 입력하세요: "))
print(type(a))
print(type(b))
print(a + b)


# 사용자로부터 태어난 연도를 입력받으면, 현재 나이를  출력하기
age = int(input("태어난 연도를 입력하세요: "))
year = int(input("현재 연도를 입력하세요: "))
print("현재나이는 {}입니다.".format(year - age + 1))

origin_pass = "1234"
input_pass = input("패스워드를 입력하세요 >>>")

if input_pass == origin_pass: # 조건 A
    # 조건 A 참
    print("로그인 성공!")
    print("반갑습니다!")
# 그렇지 않다면
else:
    print("로그인 실패, 비밀번호를 확인하세요")

origin_pass = "1234"
input_pass = input("패스워드를 입력하세요 >>>")

if input_pass == origin_pass:
    print("로그인 성공")
elif input_pass == "":
    print("아무것도 입력되지 않았습니다.")
elif input_pass == "hint":
    print("모르겠어요?")
else:
    print("잘못된 비밀번호입니다.")