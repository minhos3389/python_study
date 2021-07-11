# 상속
# : 클래스들에 중복된 코드를 제거하고 유지보수를 편하게 하기 위해서 사용.

# 부모 클래스
class Monster:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health 
        self.attack = attack 
        print(f"체력 {self.health}의 공격력이 {self.attack}인 {self.name} 몬스터 등장!")
    def move(self):
        print(f"[{self.name}] 지상으로 이동!")

# 자식 클래스
class Wolf(Monster):
    pass 
class Shark(Monster):
    def move(self): # 메서드 오버라이딩
        print(f"[{self.name}] 수영하기!")
class Dragon(Monster):
    def move(self): # 메서드 오버라이딩
        print(f"[{self.name}] 날기!")

wolf = Wolf("울프", 1500, 200)
wolf.move() 

blue_shark = Shark("푸른 상어", 10000, 300)
blue_shark.move()


red_dragon = Dragon("레드 드래곤", 20000, 500)
red_dragon.move()

