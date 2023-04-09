class RAM:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas

class Storage:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas

class Computer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

ram = RAM(32)
storage = Storage(500)
computer = Computer(ram, storage)
print(computer.ram.kapasitas)
print(computer.storage.kapasitas)