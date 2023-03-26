class Tokoh:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
    
    def get_nama(self):
        return self.nama
    
    def get_umur(self):
        return self.umur
    
    def get_alamat(self):
        return self.alamat

class Sensei(Tokoh):
    def __init__(self, nama, umur, alamat, teknik):
        super().__init__(nama, umur, alamat)
        self.teknik = teknik
    
    def get_teknik(self):
        return self.teknik

class Kage(Tokoh):
    def __init__(self, nama, umur, alamat, jutsu):
        super().__init__(nama, umur, alamat)
        self.jutsu = jutsu
    
    def get_jutsu(self):
        return self.jutsu
    
class Hokage(Kage):
    def __init__(self, nama, umur, alamat, jutsu, jeniskelamin):
        super().__init__(nama, umur, alamat, jutsu)
        self.jeniskelamin = jeniskelamin

    def get_jeniskelamin(self):
        return self.jeniskelamin

