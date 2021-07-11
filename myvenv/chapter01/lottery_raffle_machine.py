# Lottery raffle machine
# 로또 복권추첨기 만들어보기

# 1. 로또 번호 6개를 생성합니다.
# 2. 로또 번호는 1~45 까지의 랜덤 번호입니다.
# 3. 6개의 숫자 모두 달라야 합니다.

import random 

def getRandomNumber():
    number = random.randint(1, 45)
    return number


def lotto_number_maker():
    lotto_number_list = []
    while True:
        if len(lotto_number_list) != 6:
            num = getRandomNumber()
            # lotto don't allow duplication (로또번호는 중복을 허용하지 않습니다.)
            if num not in lotto_number_list:
                lotto_number_list.append(num)
        else:
            break
    # lotto_number_list.sort() lotto don't need to do sorting. (로또 번호는 오름차순 정렬할 필요가 없습니다.)
    for number in lotto_number_list:
        print(number, end=' ')

lotto_number_maker()
