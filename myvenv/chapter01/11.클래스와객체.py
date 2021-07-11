# 클래스를 사용하는 이유

champion1_name = "이즈리얼"
champion1_health = 700
champion1_attack = 90

print(f"{champion1_name}님 소환사의 협곡에 오신 것을 환영합니다.")

champion2_name = '리신'
champion2_health = 800
champion2_attack = 95

print(f"{champion2_name}님 소환사의 협곡에 오신것을 환영합니다.")

champion3_name = '야스오'
champion3_health = 920
champion3_attack = 88

print(f"{champion3_name}님 소환사의 협곡에 오신것을 환영합니다.")

def basic_attack(name, attack):
    print(f"{name} 기본공격 {attack}")

basic_attack(champion1_name, champion1_attack)
basic_attack(champion2_name, champion2_attack)

print("="*25,"클래스를 사용한 경우","="*25)

class Champion:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health 
        self.attack = attack 
        print(f"{name}님 소환사의 협곡에 오신 것을 환영합니다.")

    def basic_attack(self):
        print(f"{self.name} 기본공격 {self.attack} ")

ezreal = Champion("이즈리얼", 700, 90)
leesin = Champion("리신", 800, 95)
yasuo = Champion("야스오", 800, 95)

ezreal.basic_attack()
leesin.basic_attack()
yasuo.basic_attack()

print(yasuo)
print(yasuo.name)
print(yasuo.health)
print(yasuo.attack)

class Monster:
    def say(self):
        print("나는 몬스터다!")

goblin = Monster()
goblin.say()

# 고블린 인스턴스의 타입
print(type(goblin))

# 파이썬에서는 자료형도 클래스다.
a = 10
b = "문자열 객체"
c = True 

# 다 객체였습니다.
print(type(a))
print(type(b))
print(type(c))

# 문자열 객체 안에 있는 사용할 수 있는 메서드 확인하기
print(b.__dir__())


class Monster:
    # __init__은 인스턴스를 생성할 때 반드시 호출되는 메서드입니다.
    # 체력, 공격력,
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed 

goblin = Monster(800, 120, 300)
wolf = Monster(1500, 200, 350)