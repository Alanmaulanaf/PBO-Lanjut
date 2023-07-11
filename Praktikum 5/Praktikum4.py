data = {"Kambing": 11, "Sapi": 22, "Gajah": 43}
try:
    value = data["Ayam"]
except KeyError:
    print("Key yang dicari tidak ditemukan pada data!")