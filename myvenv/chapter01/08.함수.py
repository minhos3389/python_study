# 함수를 사용하는 경우
def printMessage(name, data):
    print(f"안녕하세요. {name}님")
    print(f"현재 프리미엄 서비스 기간이 {data}일 남았습니다.")

printMessage("김봉", 5)
printMessage("둘리", 13)

# 반환값이 있는 함수
def sum(a, b):
    return a + b

print(sum(2, 3))

import random
def getRandomNumber():
    number = random.randint(1, 10)
    return number

print(f'1~10 에서 나온 랜덤 숫자는 {getRandomNumber()} !')
print()

def multiply(a, b):
    return a * b 

print(multiply(3, 4))
print()

def printSumAvg(x, y, z):
    """
    세 개의 숫자를 받아 합계와 평균을 출력하는 함수
    """
    sum_ = x + y + z
    avg_ = int((sum_)/3)
    # 문자열 포맷팅 => f-string 사용했습니다.
    print(f"합계: {sum_}  평균: {avg_}")

printSumAvg(13, 22, 43)

# 로또 번호 추출기
# 랜덤 모듈 사용
import random

def get_random_number():
    """
    1 부터 45 에서 랜덤 정수를 추출하는 함수
    number : random.randint함수로 추출된 정수
    """
    number = int(random.randint(1, 45))
    return number

lotto_num_list = [] # 리스트생성

# for i in range(6):
#     random_number = get_random_number() 
#     lotto_num_list.append(random_number)

count = 0 # 현재 뽑은 숫자 개수
while True:
    random_number = get_random_number()
    if count == 6:
        # 리스트 정렬
        lotto_num_list.sort()
        break

    if random_number not in lotto_num_list:
        lotto_num_list.append(random_number)
        count += 1


for num in lotto_num_list:
    print(num, end=" ")    
    

