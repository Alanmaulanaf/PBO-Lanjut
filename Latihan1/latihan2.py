
"""Contoh2"""
class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    def info(self):
        print(f"Nama: {self.nama}\nNIM: {self.npm}")
mahasiswa1 = Mahasiswa("Alan Maualana Fajar", "210511037")
mahasiswa1.info()