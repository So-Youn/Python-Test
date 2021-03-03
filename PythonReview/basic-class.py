# __init__ : 파이썬에서 쓰이는 생성자 (자동 호출)
# 멤버 변수 : 클래스 내에서 정의된 변수 --  self.xx
class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

marine1 = Unit("마린",40,5) # self 제외하고 적어줌
marine2 = Unit("마린",40,5)
tank = Unit("탱크", 150,35)
# marine3 = Unit("마린") -> 오류 발생

# 멤버변수 외부에서 사용해서 호출
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("레이스", 80, 5)
wraith2.clocking = True # 객체에 변수 추가 할당

if wraith2.clocking == True:
    print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))


