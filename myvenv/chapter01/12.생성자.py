# 생성자
# : 인스턴스(객체가 인스턴스를 포함)를 만들 때 호출되는 메서드

class Monster:
    def __init__(self, health, attack, speed):
        self.health = health
        self.attack = attack
        self.speed = speed 
    def decrease_health(self, num):
        self.health -= num 
    def get_health(self):
        return self.health 

# 고블린 인스턴스 생성
# 체력 800, 공격력 120, 스피드 300
goblin = Monster(800, 120, 300)
goblin.decrease_health(100)
print(f'goblin의 남은 체력은 {goblin.get_health()}')

# 늑대 인스턴스 생성
wolf = Monster(1500, 200, 350)
wolf.decrease_health(1000)
print(f'wolf의 남은 체력은 {wolf.get_health()}')

