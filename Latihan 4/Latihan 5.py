class Whell:
    def __init__(self, size):
        self.size = size

class Engine:
    def __init__(self, power):
        self.power = power

class Car:
    def __init__(self, whells, engine):
        self.whells = whells
        self.engine = engine

whell1 = Whell(11)
whell2 = Whell(11)
whell3 = Whell(11)
whell4 = Whell(11)
engine = Engine(100)
car = Car([whell1, whell2, whell3, whell4], engine)
print(car.whells[0].size)

