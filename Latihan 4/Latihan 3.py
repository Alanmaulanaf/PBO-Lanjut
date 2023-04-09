class Menu:
    def __init__(self,menu, dishes=None):
        if dishes is None:
            self.dishes = []
        
        else:
            self.dishes = dishes
        
        self.menu = menu

    def add_dish(self, dish):
        self.dishes.append(dish)
    
    def __repr__(self):
        return f'{self.menu}'
    
class Dish:
    def __init__(self, nama, harga):
        self.nama = nama
        #print(f"Nama: ",self.nama)
        self.harga = harga
        #print(f"Harga: ",self.harga)
    
    def __repr__(self):
        return f'{self.nama} {self.harga}'
    
class Restaurant:
    def __init__(self, nama, menu):
        self.nama = nama
        print(f'Nama: ',self.nama)
        self.menu = menu
        print(self.menu)

dish1 = Dish("Nasi Goreng", "Rp.15.000")
dish2 = Dish("Soto Malang", "Rp.20.000")
menu = Menu([dish1,dish2])
restaurant = Restaurant("Warteg", menu)
restaurant.menu.dishes