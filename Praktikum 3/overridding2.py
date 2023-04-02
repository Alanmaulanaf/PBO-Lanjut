from abc import ABC, abstractmethod

class Kendaraan(ABC):
    @abstractmethod
    def mulai(self):
        pass

class Motor(Kendaraan):
    def mulai(self):
        print("menyalakan motor")

class Mobil(Kendaraan):
    def mulai(self):
        print("menyalakan mobil")

class Sepeda(Kendaraan):
    def mulai(self):
        print("mengayuh sepeda")

kendaraan = [Motor(), Mobil(), Sepeda()]

for kendaraaan in kendaraan:
    kendaraaan.mulai()