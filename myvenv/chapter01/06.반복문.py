# 반복문
# :반복해서 명령을 사용하고 싶을 때

# 시퀀스 자료형
# : 순서가 있는 자료형
# 1. 리스트
# 2. 문자열 
# 3. range객체
# 4. 튜플
# 5. 딕셔너리

# for문
# - 리스트 사용
champions = ['티모', '이즈리얼', '리신']

for champion in champions:
    print("선택한 챔피언은", champion, "입니다. ")
print("for 문 종료")

# 문자열 사용
fighting_message = "자신감을 가지자!"

for word in fighting_message:
    print(word)
# 자
# 신
# 감
# 을 
#
# 가
# 지
# 자
# ! 
 
# -range 객체 사용
# 1~9까지 줄바뀌면서 출력
for i in range(10):
    print(i) 

# range(시작, 끝+1, 단계) 으로 입력
# 1,3,5,7,9 줄바뀌면서 출력 
for i in range(1, 11, 2):
    print(i)

# while
# : 보통 반복 횟수가 정해지지 않았을 때 사용합니다.

i = 5 # 초기식
while i < 10: # 조건식
    print(i, "번째 다짐, 나는 할 수 있다!")
    i += 2 # 2씩 증감

# 무한 루프
# 조건식에 True를 넣어서 항상 반복되게 만드는 것.
while True:
    x = input("종료하려면 exit을 입력하세요 >>>")
    if x == "exit":
        print("무한루프가 종료됩니다.")
        break

# 구구단 출력문제

while True:
    gugudan = int(input("몇 단을 출력할까요?"))
    if 0 < gugudan < 10:
        print("단이 입력되었습니다. ")
        break


for i in range(1, 10):
    print(f'{gugudan}*{i}={gugudan*i}')

while True:
    print(
        """
        [메뉴를 입력하세요]
        1. 게임시작
        2. 실시간 랭킹
        3. 게임종료
        """
    )
    game_input = int(input("숫자를 입력해주세요 >>> "))
    if game_input == 1:
        print("게임을 시작합니다.\n")
    elif game_input == 2:
        print("실시간 랭킹\n")
    elif game_input == 3:
        print("게임을 종료합니다.\n")
        break
    else:
        print("다시 입력해주세요\n")