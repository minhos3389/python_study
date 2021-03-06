# 주석
'''
주석 # ,여러줄 주석 
1. 코드에 설명을 추가하고 싶을 떄
2. 코드를 실행하고 싶지 않을 때
'''

# - 숫자 자료형
# 1. 정수형 : 소수점이 없는 수
print(1)
print(3)
print(0)
print(-1)

# 2. 실수형 : 소수점이 있는 수
# , 를 이용하여 간격에 공백을 줘서 출력할 수 있습니다.
print(1.1)
# 공백제거
print(1, 3, 0, -1)
print(1, 3, 0, -1, sep="")
# 간격 사이에 * 을 넣어서 출력
print(1, 3, 0, -1, sep="*")


# - 문자열 자료형
# " " or ''

print('파이썬 너무 재밌다.')
# end 옵션을 통해서 다음 출력문과 연결을 수행할 수 있습니다.
print("파이썬은 너무 좋은 언어예요!", end='')
print('아저씨가 "개 짖는 소리좀 안나게 해라!" 라고 말했다.')
# [출력 결과]
# 파이썬은 너무 좋은 언어예요!아저씨가 "개 짖는 소리좀 안나게 해라!" 라고 말했다. 

name = 'kimchi jjang!'
if name.startswith('kimchi'):
    print('문장이 kimchi 로 시작해요')