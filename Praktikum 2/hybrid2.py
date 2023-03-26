class Transportasi:
    def __init__(self, type, warna, nopol):
        self.type = type
        self.warna = warna
        self.nopol = nopol
    
    def Info_Masseh(self):
        print("Type: ", self.type)
        print("Warna: ", self.warna)
        print("Nopol: ", self.nopol)

class Umum(Transportasi):
    def __init__(self, type, warna, nopol, merk):
        super().__init__(type, warna, nopol)
        self.merk = merk
    
    def Info_Masseh(self):
        super().Info_Masseh()
        print("Merk: ",self.merk)

class Pribadi(Transportasi):
    def __init__(self, type, warna, nopol, jenis):
        super().__init__(type, warna, nopol, jenis)
        self.jenis = jenis

    def Info_Masseh(self):
        super().Info_Masseh()
        print("Jenis: ",self.jenis)

class Kendaraan(Pribadi, Umum):
    def __init__(self, type, warna, nopol, merk, jenis, no_mesin):
        Pribadi.__init__(self, type, warna, nopol, jenis)
        Umum.__init__(self, type, warna, nopol, merk)
        self.no_mesin = no_mesin
    
    def Info_Masseh(self):
        super().Info_Masseh()
        print("No.Mesin: ",self.no_mesin)

kendaraan = Kendaraan("QWERTY", "Hitam", "A L4N MF", "Yahaha", "Sepeda Motor", 123456789)
kendaraan.Info_Masseh()