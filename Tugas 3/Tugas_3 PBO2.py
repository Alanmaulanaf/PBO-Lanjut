from playsound import *


class Animal:
    def make_sound(self):
        print("Suara")
    
class Anjing(Animal):
    def make_sound(self):
        print("anjing")
        playsound('anjing.mp3')

class Kucing(Animal):
    def make_sound(self):
        print("Kucing")
        playsound('kucing.mp3')

class Ayam(Animal):
    def make_sound(self):
        print("Ayam")
        playsound('ayam.mp3')

class Babi(Animal):
    def make_sound(self):
        print("Babi")
        playsound('babi.mp3')

class Kambing(Animal):
    def make_sound(self):
        print("Kambing")
        playsound('kambing.mp3')

class Harimau(Animal):
    def make_sound(self):
        print("Harimau")
        playsound('harimau.mp3')

class Tokek(Animal):
    def make_sound(self):
        print("Tokek")
        playsound('tokek.mp3')

class Sapi(Animal):
    def make_sound(self):
        print("Sapi")
        playsound('sapi.mp3')

class Serigala(Animal):
    def make_sound(self):
        print("Serigala")
        playsound('serigala.mp3')

class Singa(Animal):
    def make_sound(self):
        print("Singa")
        playsound('singa.mp3')


def animal_sound(Animal):
    Animal.make_sound()

hewan = Animal()
anjing = Anjing()
kucing = Kucing()
ayam = Ayam()
babi = Babi()
kambing = Kambing()
harimau = Harimau()
tokek = Tokek()
sapi = Sapi()
serigala = Serigala()
singa = Singa()

animal_sound(anjing)