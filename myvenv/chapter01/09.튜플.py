#  튜플 만들기 

tuple_a = (3, 4, 5)
print(tuple_a)

tuple_b = 3, 4, 5
print(tuple_b)

# 튜플을 리스트로 만들기

tuple_c = tuple([5, 6, 7])
print(tuple_c) # (5, 6, 7)

list_d = list(range(10))
print(list_d) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

tuple_d = tuple(list_d)
print(tuple_d) # (1, 2, 3, 4, 5, 6, 7, 8, 9)

tuple_e = 5, 6, 7
list_e = [tuple_e] # [5, 6, 7]

# 패킹과 언패킹
numbers = 3, 4, 5 # 패킹
a, b, c = numbers # 언패킹
print(a, b, c)

a = 10, 20, 30, 40, 30
print(a.index(20)) # 1
print(a.count(30)) # 2
print(max(a), min(a)) # (40, 10)
print(sum(a)) # 130

# 튜플
# : 읽기 전용 리스트

a = (3, 4, 5)
b = 3, 4, 5

c=  (3, )
d = 3,

e = tuple([3, 4, 5])
f = list(range(10))
g = tuple(f)

h = 3, 4, 5
i = list(h)

# 튜플 관련함수
x = 4, 5, 2, 3, 4
print(max(x)) # 5
print(min(x)) # 2
print(x.count(4)) # 4라는 요소 값 2개
print(x.index(4)) # 가장 첫번째 4의 인덱스만 반환