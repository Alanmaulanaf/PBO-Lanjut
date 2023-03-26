class Mahkluk:
    def __init__(self, Nama):
        self.Nama = Nama
    
    def Berbicara(self):
        print(f"{self.Nama} berbicara sendiri")

class Orang(Mahkluk):
    def __init__(self, Nama, Kulit):
        super().__init__(Nama)
        self.Kulit = Kulit
    
    def Bertanya(self):
        print(f"{self.Nama} kulitnya {self.Kulit}")

class Siswa(Orang):
    def __init__(self, Nama, Kulit, Bahasa):
        super().__init__(Nama, Kulit)
        self.Bahasa = Bahasa
    
    def Berbicara(self):
        print(f"{self.Nama} berbicara bahasa {self.Bahasa}")
        
siswa = Siswa("Alan Maulana Fajar", "Hitam", "Sunda")
siswa.Berbicara()
siswa.Bertanya()