class PersonalComputer:
    def __init__(self, Merk, CPU, GPU):
        self.Merk = Merk
        self.CPU = CPU
        self.GPU = GPU
    
    def Spesifikasi(self):
        print(f"Merk: {self.Merk}")
        print(f"CPU: {self.CPU}")
        print(f"GPU: {self.GPU}")

class Monitor:
    def __init__(self, Layar, Refreshrate):
        self.Layar = Layar
        self.Refreshrate = Refreshrate

    def Spesifikasi(self):
        print(f"Layar: {self.Layar}")
        print(f"Refreshrate: {self.Refreshrate}")
    
class Power:
    def __init__(self, Battery, Kapasitas):
        self.Battery = Battery
        self.Kapasitas = Kapasitas
    
    def Spesifikasi(self):
        print(f"Battery: {self.Battery}")
        print(f"Kapasitas: {self.Kapasitas}")

class Laptop(Monitor,Power):
    def __init__(self, Merk, CPU, GPU, Layar, Refreshrate, Battery, Kapasitas):
        PersonalComputer.__init__(self, Merk, CPU, GPU)
        Monitor.__init__(self, Layar, Refreshrate)
        Power.__init__(self, Battery, Kapasitas)
    
    def Spesifikasi(self):
        print(f"Merk: {self.Merk}")
        print(f"CPU: {self.CPU}")
        print(f"GPU: {self.GPU}")
        super().Spesifikasi()
        print(f"Battery: {self.Battery}")
        print(f"Kapasitas: {self.Kapasitas}")

laptop = Laptop("Lenovo Legion 5 Pro", "AMD Ryzen 7 5800H", "GForce RTX 3090", "Full QHD", "170Hz", "li-ion", "7000")
laptop.Spesifikasi()