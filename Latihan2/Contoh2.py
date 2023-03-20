class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
    def tugas(self):
        print(self.nama, "sedang mengerjakan tugas")

class Pekerja:
    def __init__(self, nama, belajar):
        self.nama = nama
        self.belajar = belajar
    def skripsi(self):
        print(self.nama, "sedang belajar skripsi")

class MahasiswaPekerja(Mahasiswa, Pekerja):
    def __init__(self, nama, nim, belajar):
        Mahasiswa.__init__(self, nama, nim)
        Pekerja.__init__(self, nama, belajar)
    def bersosialisasi(self):
        print(self.nama, "sedang bersosialisasi")

mhs_pekerja = MahasiswaPekerja("Alan", "210511037", "Programmer")
mhs_pekerja.tugas() 
mhs_pekerja.skripsi() 
mhs_pekerja.bersosialisasi() 