class Hewan:
    def suara(self):
        print("hewan membuat sebuah suara")

class kucing(Hewan):
    def suara(self):
        print("Meaowwww Meaowwwww")

class anjing(Hewan):
    def suara(self):
        print("Gukkk Gukkkk")

class sapi(Hewan):
    def suara(self):
        print("Moooo Mooooo")

def hewan_suara(hewan):
    hewan.suara()

hewan = Hewan()
Kucing = kucing()
Anjing = anjing()
Sapi = sapi()

hewan_suara(hewan)
hewan_suara(Kucing)
hewan_suara(Anjing)
hewan_suara(Sapi)