import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__Kode_buku = None
        self.__Judul = None
        self.__Penulis = None
        self.__Penerbit = None
        self.__Tahun_terbit = None
        self.__Stok = None
        self.__url = "http://localhost/Perpustakaan/buku_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def Kode_buku(self):
        return self.__Kode_buku
        
    @Kode_buku.setter
    def Kode_buku(self, value):
        self.__Kode_buku = value
    @property
    def Judul(self):
        return self.__Judul
        
    @Judul.setter
    def Judul(self, value):
        self.__Judul = value
    @property
    def Penulis(self):
        return self.__Penulis
        
    @Penulis.setter
    def Penulis(self, value):
        self.__Penulis = value
    @property
    def Penerbit(self):
        return self.__Penerbit
        
    @Penerbit.setter
    def Penerbit(self, value):
        self.__Penerbit = value
    @property
    def Tahun_terbit(self):
        return self.__Tahun_terbit
        
    @Tahun_terbit.setter
    def Tahun_terbit(self, value):
        self.__Tahun_terbit = value
    @property
    def Stok(self):
        return self.__Stok
        
    @Stok.setter
    def Stok(self, value):
        self.__Stok = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_Kode_buku(self, Kode_buku):
        url = self.__url+"?Kode_buku="+Kode_buku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['Id_buku']
            self.__Kode_buku = item['Kode_buku']
            self.__Judul = item['Judul']
            self.__Penulis = item['Penulis']
            self.__Penerbit = item['Penerbit']
            self.__Tahun_terbit = item['Tahun_terbit']
            self.__Stok = item['Stok']
        return data
    def simpan(self):
        payload = {
            "Kode_buku":self.__Kode_buku,
            "Judul":self.__Judul,
            "Penulis":self.__Penulis,
            "Penerbit":self.__Penerbit,
            "Tahun_terbit":self.__Tahun_terbit,
            "Stok":self.__Stok
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_Kode_buku(self, Kode_buku):
        url = self.__url+"?Kode_buku="+Kode_buku
        payload = {
            "Kode_buku":self.__Kode_buku,
            "Judul":self.__Judul,
            "Penulis":self.__Penulis,
            "Penerbit":self.__Penerbit,
            "Tahun_terbit":self.__Tahun_terbit,
            "Stok":self.__Stok
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_Kode_buku(self,Kode_buku):
        url = self.__url+"?Kode_buku="+Kode_buku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
