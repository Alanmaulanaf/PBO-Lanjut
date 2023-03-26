class Makanan:
    def __init__(self, Nama, Jenis):
        self.Nama = Nama
        self.Jenis = Jenis
    
    def dessert(self):
        print(self.Nama, "Sangat Enak!!!")

class Bakso(Makanan):
    def __init__(self, Nama, Jenis, Harga):
        super().__init__(Nama, Jenis)
        self.Harga = Harga  
    
    def Appetizer(self): 
        print("Ayam Geprek",self.Harga)

bakso = Bakso("Bakso Mercon", "Kuah", "10.000")
bakso.dessert()
bakso.Appetizer()