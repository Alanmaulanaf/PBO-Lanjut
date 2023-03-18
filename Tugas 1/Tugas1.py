print("Nama : Alan Maulana Fajar ")
print("NIM  : 210511037 ")
print("Kelas: R1 ")
print(           "=" *30        )

class Fahrenheit:
    def __init__(self, Fahrenheit):
        self.Fahrenheit = Fahrenheit
    
    def Reamur(self):
        return 4/9 *(self.Fahrenheit - 32)

    def Kelvin(self):
        return 5/9 *(self.Fahrenheit - 32) + 273

class Reamur:
    def __init__(self, Reamur):
        self.Reamur = Reamur
    
    def Fahrenheit(self):
        return (9/4 * self.Reamur)+ 32
    
    def Kelvin(self):
        return 5/4 * self.Reamur + 273

class Kelvin:
    def __init__(self, Kelvin):
        self.Kelvin = Kelvin

    def Fahrenheit(self):
        return 9/5 * (self.Kelvin - 273) + 32

    def Reamur(self):
        return 4/5 * (self.Kelvin - 273)

Fahrenheit1 = Fahrenheit(70)
print(f"Konversi Fahrenheit ke Reamur : {Fahrenheit1.Reamur()}")
Fahrenheit2 = Fahrenheit(60)
print(f"Konversi Fahrenheit Ke Kelvin: {Fahrenheit2.Kelvin()}")
print("="*50)

Reamur1 = Reamur(60)
print(f"Konversi Reamur ke Fahrenheit: {Reamur1.Fahrenheit()}")
Reamur2 = Reamur(70)
print(f"Konversi Reamur ke Kelvin: {Reamur2.Kelvin()}")
print("="*50)

Kelvin1 = Kelvin(70)
print(f"Konversi Kelvin ke Fahrenheit: {Kelvin1.Fahrenheit()}")
Kelvin2 = Kelvin(80)
print(f"Konversi Kelvin ke Reamur: {Kelvin2.Reamur()}")
