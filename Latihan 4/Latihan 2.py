class Player:
    def __init__(self, nama):
        self.nama = nama
        print(f"Player: ",self.nama)
        self.inventory = Inventory()

class Item:
    def __init__(self, nama):
        self.nama = nama
        print(f"Item: ",self.nama)

    def __repr__(self):
        return f'{self.nama}'
        
class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
    
    def remove_item(self, item):
        self.items.remove(item)
    

player = Player("Alan")
sword = Item("Sword")
shield = Item("Shield")
player.inventory.add_item(sword)
player.inventory.add_item(shield)
print(player.inventory.items)