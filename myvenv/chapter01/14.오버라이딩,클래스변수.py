import random

class Monster:
    # 몬스터 최대 제한 마릿수
    max_num = 1000
    
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health 
        self.attack = attack
        # 클래스 변수를 사용할 때는 self 가 아닌 클래스명.변수명 사용 
        Monster.max_num -= 1
    def move(self):
        print(f"[{self.name}이 지상으로 이동]")
    
class Wolf(Monster):
    pass
class Shark(Monster):
    def move(self):
        print(f"[{self.name}]이 헤엄칩니다!")
class Dragon(Monster):
    # 생성자 오버라이딩
    def __init__(self, name, health, attack):
        # 부모 클래스를 불러올 수 있으며, 부모 클래스의 인자들도 불러올 수 있습니다.
        super().__init__(name, health, attack)
        # 새로 추가하는 Dragon 클래스의 속성값
        self.skill = ("불뿜기", "날개치기", "꼬리공격")
    def move(self):
        print(f"[{self.name}]이 날아갑니다!")
    def skills(self):
        print(f"[{self.name}] 스킬 사용 {self.skill[random.randint(0, 2)]}")

wolf = Wolf("울프", 100, 30)
wolf.move()
print(wolf.max_num)

shark = Shark("상어", 1000, 100)
shark.move()
print(shark.max_num)

dragon = Dragon("드래곤", 2000, 300)
print(dragon.max_num)
dragon.move()
dragon.skills()