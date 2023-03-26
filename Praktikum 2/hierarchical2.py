class Keluarga:
    def __init__(self, nama):
        self.nama = nama
    
    def get_nama(self):
        print(self.nama)
    
class Orangtua(Keluarga):
    def __init__(self, nama, umur):
        super().__init__(nama)
        self.umur = umur
    
    def get_umur(self):
        print(self.umur)

class Anak(Keluarga):
    def __init__(self, nama, jeniskelamin):
        super().__init__(nama)
        self.jeniskelamin = jeniskelamin

    def get_jeniskelamin(self):
        print(self.jeniskelamin)

class Cucu(Orangtua):
    def __init__(self, nama, umur, alamat):
        super().__init__(nama, umur)
        self.alamat = alamat

    def get_alamat(self):
        print(self.alamat)

class Buyut(Anak):
    def __init__(self, nama, jeniskelamin, hobby):
        super().__init__(nama, jeniskelamin)
        self.hobby = hobby

    def get_hobby(self):
        print(self.hobby)

print("Bagian Cucu")
cucu = Cucu("alan","20","Kuningan")
cucu.get_nama()
cucu.get_umur()
cucu.get_alamat()
print("="*30)
print("Bagian Buyut")
buyut = Buyut("maulana", "laki-laki", "Ngegame")
buyut.get_nama()
buyut.get_jeniskelamin()
buyut.get_hobby()