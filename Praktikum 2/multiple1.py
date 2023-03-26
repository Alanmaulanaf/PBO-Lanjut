class Menteri:
    def __init__(self, Nama, Alamat):
        self.Nama = Nama
        self.Alamat = Alamat
    
    def Tugas(self):
        print(self.Nama, "sedang bertugas")

class Pajak:
    def __init__(self, Nama, gaji):
        self.Nama = Nama
        self.gaji = gaji
    
    def sosialisali(self):
        print(self.Nama,"sedang bersosialisasi dengan gaji",self.gaji)

class MenteriPajak(Menteri, Pajak):
    def __init__(self, Nama, Alamat, gaji):
        Menteri.__init__(self, Nama, Alamat)
        Pajak.__init__(self, Nama, gaji)

    def beristirahat(self):
        print(self.Nama,"sedang tidur dikamar")

pejabat = MenteriPajak("Alan Maulana Fajar", "Kuningan", "Rp.100.000.000")
pejabat.Tugas()
pejabat.sosialisali()
pejabat.beristirahat()