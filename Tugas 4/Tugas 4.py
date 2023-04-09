print("Alan Maulana Fajar")
print("210511037")
print("Kelas R1")
print("="*40)

class Hewan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        self.informasi = Informasi()
    
    def __repr__(self):
        return f'Nama: {self.nama}\nJenis: {self.jenis}'

class Informasi:
    def __init__(self):
        self.info = []
    
    def add_informasi(self, warna, spesies):
        self.info.append(warna)
        self.info.append(spesies)
    
    def delete_informasi(self, warna, spesies):
        self.info.remove(warna)
        self.info.remove(spesies)

class Banteng:
    def __init__(self, hewan):
        self.hewan = hewan

hewan = Hewan("Banteng Always Win", "Omnivora")
info = Informasi()
hewan.informasi.add_informasi("Warna: Merah","Spesies: Legendary")
print(repr(hewan))
print(hewan.informasi.info)
