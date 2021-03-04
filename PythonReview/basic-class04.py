class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flayble:
    def __init__(self):
        print("Flyable 생성자")

class FlaybleUnit(Unit, Flayble):
    def __init__(self):
        # 다중상속 시에는 super X
        # super().__init__()
        Unit.__init__(self)
        Flayble.__init__(self)

dropship = FlaybleUnit()