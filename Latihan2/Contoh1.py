class Hewan:
    def __init__(self, nama, warna):
        self.nama = nama
        self.warna = warna

    def bergerak(self):
        print(self.nama, "Bergerak")

class Anjing(Hewan):
    def __init__(self, nama, warna, jenis_anjing):
        super().__init__(nama,warna)
        self.jenis_anjing = jenis_anjing
    
    def bersuara(self):
        print("Moooooo!!!")
    
anjingA = Anjing("Doggy","Hitam","BullDog")
anjingA.bergerak()
anjingA.bersuara()