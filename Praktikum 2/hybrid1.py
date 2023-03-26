class Grup:
    def __init__(self, Nama, Umur):
        self.Nama = Nama
        self.Umur = Umur
    
    def Info(self):
        print("Identitas\nNama: ",self.Nama)
        print("Umur: ", self.Umur)
    
class Membership(Grup):
    def __init__(self, Nama, Umur, Status):
        super().__init__(Nama, Umur)
        self.Status = Status

    def Info(self):
        super().Info()
        print("Status: ",self.Status)

class Anggota(Grup):
    def __init__(self, Nama, Umur, Jenis_Membership):
        super().__init__(Nama, Umur, Jenis_Membership)
        self.Jenis_Membership = Jenis_Membership
    
    def Info(self):
        super().Info() 
        print("Jenis_Membership: ", self.Jenis_Membership)

class Orang(Anggota, Membership):
    def __init__(self, Nama, Umur, Status, Jenis_Membership, Alamat):
        Anggota.__init__(self, Nama, Umur, Jenis_Membership)
        Membership.__init__(self, Nama, Umur, Status)
        self.Alamat = Alamat

    def Info(self):
        super().Info()
        print("Alamat: ",self.Alamat)

orang = Orang("Alan Maulana Fajar", "20", "Aktif", "Platinum", "Kuningan")
orang.Info()