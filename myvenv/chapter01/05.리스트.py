a = [1, 2, 3]
a.append(4)
print(a) # [1, 2, 3, 4]
a[0] = 0 
print(a) # [0, 2, 3, 4]
del a[0]
print(a) # [2, 3, 4]

b = [3, 4, 2, 6]
b.sort()
print(b) # [2, 3, 4, 6]


# 리스트 만들기
players = ['손흥민', '알리', '케인']

# 데이터가 없는 리스트
buy_list = []

# 데이터 접근하기
players[0]  # 가장 첫번째 데이터 
players[-1]  # 가장 마지막 데이터 

# 데이터 추가하기
players.append('토미야스')
print(players)

# 데이터 삭제하기
del players[2]
print(players) #['손흥민', '알리', '토미야스']

# 리스트 슬라이싱
print(players[:2]) # 인덱스 0 부터 1까지
print(players[:]) # 전체
print(players[1:]) # 인덱스1부터 끝까지
print(players[::-1]) # 역순 출력

# 리스트 길이
print(len(players))
# 리스트 정렬
players.sort(reverse=True) # 역순정렬
print(players)
players.sort() # 정렬 (ㄱ-ㄴ-ㄷ 순.)
print(players)

result = [33, 40, 12, 63, 52]
result.append(9)
result[1] = 50
print(result)
print(result[2:])  
print(sorted(result)) # 오름차순 정렬 (sorted()는 새로운 객체 반환)

pull_up_list = []
num = 0
for i in range(1,8):
    pull_up_list.append(int(input("{}일차 턱걸이 횟수 >>>".format(i))))

print(f'턱걸이 리스트: {pull_up_list}')
# total = data[0] + data[1] + data[2] + data[3] + data[4] + data[5] + data[6]
# print(int(total / 7))) 

print(f"평균 턱걸이 갯수는:{int(sum(pull_up_list)/7)} 개 입니다.")




