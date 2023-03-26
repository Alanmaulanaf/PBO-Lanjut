class Makanan:
    def __init__(self, nama):
        self.nama = nama
    
    def Rasa(self):
        print(f"{self.nama} rasanya enak")
    
class Buah(Makanan):
    def __init__(self, nama, warna):
        super().__init__(nama)
        self.warna = warna
    
    def Rasa(self):
        print(f"Buah ini {self.warna}")

class Apel(Buah):
    def __init__(self, nama, warna, asal):
        super().__init__(nama, warna)
        self.asal = asal
    
    def Rasa(self):
        print(f"Apel dari {self.asal}")

apel = Apel("Apel", "Merah", "Malang")
apel.Rasa()