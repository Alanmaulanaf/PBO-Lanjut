class Pakaian:
    def __init__(self, Merk, Ukuran):
        self.Merk = Merk
        self.Ukuran = Ukuran
    
    def memakai(self):
        print(self.Merk, " Berwarna Hitam")
    
class Kemeja(Pakaian):
    def __init__(self, Merk, Ukuran, Harga):
        super().__init__(Merk, Ukuran)
        self.Harga = Harga
    
    def model(self):
        print(self.Harga,"Untuk Tangan Panjang")
    
kemeja = Kemeja("Gabriel", "L", "Rp.500.000")
kemeja.memakai()
kemeja.model()