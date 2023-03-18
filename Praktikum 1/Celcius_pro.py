print("Nama : Alan Maulana Fajar ")
print("NIM  : 210511037 ")
print("Kelas: R1 ")
print(            "=" *30            )

class Celcius:
    @staticmethod
    def ke_Fahrenheit(celcius):
        return (celcius * 9/5) + 32

    @staticmethod
    def ke_Reamur(celcius):
        return celcius * 4/5

    @staticmethod
    def ke_Kelvin(celcius):
        return celcius + 273
    
celcius1 = 75
celcius2 = 60
celcius3 = 90

Fahrenheit = Celcius.ke_Fahrenheit(celcius1)
print("Konversi",celcius1,"derajat celcius adalah ",Fahrenheit," derajat fahrenheit")
print("="*61)  
Reamur = Celcius.ke_Reamur(celcius2)
print("Konversi",celcius2,"derajat celcius adalah ",Reamur," derajat reamur")
print("="*61) 
Kelvin = Celcius.ke_Kelvin(celcius3)
print("Konversi",celcius3,"derajat celcius adalah ", Kelvin ," derajat kelvin")
print("="*61) 
