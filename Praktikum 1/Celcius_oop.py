print("Nama : Alan Maulana Fajar ")
print("NIM  : 210511037 ")
print("Kelas: R1 ")
print(           "=" *30        )

class KonversiCelcius:
    def __init__(self, Celcius):
        self.celcius = Celcius

    def Fahrenheit(self):
        return (self.celcius * 9/5) + 32
    def Reamur(self):
        return self.celcius * 4/5
    def Kelvin(self):
        return self.celcius + 273

celcius1 = KonversiCelcius(75)
print(f"Konversi Celcius Ke Fahrenheit: {celcius1.Fahrenheit()}")
celcius2 = KonversiCelcius(60)
print(f"KOnversi Celcius Ke Reamur: {celcius2.Reamur()}")
celcius3 = KonversiCelcius(90)
print(f"Konversi Celcius Ke Kelvin: {celcius3.Kelvin()}")