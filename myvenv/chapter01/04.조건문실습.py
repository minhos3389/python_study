# subscriber_number = int(input("현재 구독자 수를 입력하세요>>>"))
# if subscriber_number >= 1000:
#     print("수익 창출이 가능합니다!")
# else:
#     print("수익 창출이 불가능합니다!")

# study_time = int(input("공부시간을 입력하세요(시간) >>>"))
# if study_time >= 10:
#     print("휴대폰 잠금이 해제됩니다.")
# elif study_time >= 5:
#     print("휴대폰을 30분간 사용가능합니다.")
# else:
#     print("휴대폰 사용이 불가능합니다.")

# money = int(input("현재 가진 금액을 입력 >>>"))
# if money >= 20000:
#     print("오늘 저녁은 ... 치킨!")
# elif  money >= 10000:
#     print("오늘 저녁은 ... 떡볶이!")
# elif money >= 2000:
#     print("오늘 저녁은 ... 편의점 김밥!")
# else:
#     pass 


korean_score = int(input("국어성적을 입력해주세요 >>> "))
english_score = int(input("영어성적을 입력해주세요 >>> "))
math_score = int(input("수학성적을 입력해주세요 >>> "))

avg = (korean_score + english_score + math_score) / 3

# solution 1
if 0 <= korean_score <= 100 and 0 <= math_score <= 100 and 0 <= english_score <= 100:
    if avg >= 80:
        print("합격")
    else:
        print("불합격")
else:
    print("잘못 입력하였습니다.")

# solution 2
if korean_score < 0 or korean_score > 100 or math_score < 0 or math_score > 100 or english_score < 0 or english_score > 100:
    print("잘못 입력되었습니다.")
else:
    if avg >= 80:
        print("합격")
    else:
        print("불합격")