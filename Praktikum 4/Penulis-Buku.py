print("Alan Maulana Fajar")
print("210511037")
print("Kelas R1")
print("="*40)

class Penulis:
    def __init__(self, nama, judul):
        self.nama = nama
        self.judul = judul
        self.informasi = Informasi()
    
    def __repr__(self):
        return f'{self.nama}'
        return f'{self.judul}'

class Informasi:
    def __init__(self):
        self.info = []
    
    def add_informasi(self, penerbit, harga):
        self.info.append(penerbit)
        self.info.append(harga)
    
    def delete_informasi(self, penerbit, harga):
        self.info.remove(penerbit)
        self.info.remove(harga)

class Buku:
    def __init__(self, penulis):
        self.penulis = penulis

penulis = Penulis("Alan Maulana Fajar", "Hengker Tzy")
info = Informasi()
penulis.informasi.add_informasi(2023, "Rp.50.000")
print(repr(penulis))
print(penulis.informasi.info)
