class PersonMeta(type):
    def __init__(cls, name, age, attrs):
        super().__init__(name,age, attrs)

        def data(cls,name,age):
            print(name, age)
        cls.data = classmethod(data)

class Person(metaclass=PersonMeta):
    pass

A=Person()
B=A.data('Udin',25)
print("data: ",B)

# Menambah atribut address secara dinamis
A.address = "Jalan Siliwangi"

print(A.address)

def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

weight = float(input("Inputkan berat badan (kg): "))
height = float(input("Inputkan tinggi badan (m): "))

hasil_bmi = calculate_bmi(weight, height)
print("Berat Badan Anda adalah: ",hasil_bmi)

if hasil_bmi < 19.5:
    print("Anda termasuk dalam kategori Underweight (Kurus)")
elif 19.5 <= hasil_bmi < 30:
    print("Anda termasuk dalam kategori Normal (Ideal)")
elif 30 <= hasil_bmi < 35:
    print("Anda termasuk dalam kategori Overweight (Kelebihan Berat Badan)")
else:
    print("Anda termasuk dalam kategori Obese (Kegemukan)")