import requests
import json
class Kategori:
    def __init__(self):
        self.__id=None
        self.__Kode_Kategori = None
        self.__Jenis = None
        self.__Id_buku = None
        self.__url = "http://localhost/Perpustakaan/kategori_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def Kode_Kategori(self):
        return self.__Kode_Kategori
        
    @Kode_Kategori.setter
    def Kode_Kategori(self, value):
        self.__Kode_Kategori = value
    @property
    def Jenis(self):
        return self.__Jenis
        
    @Jenis.setter
    def Jenis(self, value):
        self.__Jenis = value
    @property
    def Id_buku(self):
        return self.__Id_buku
        
    @Id_buku.setter
    def Id_buku(self, value):
        self.__Id_buku = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_Kode_Kategori(self, Kode_Kategori):
        url = self.__url+"?Kode_Kategori="+Kode_Kategori
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['Id_Kategori']
            self.__Kode_Kategori = item['Kode_Kategori']
            self.__Jenis = item['Jenis']
            self.__Id_buku = item['Id_buku']
        return data
    def simpan(self):
        payload = {
            "Kode_Kategori":self.__Kode_Kategori,
            "Jenis":self.__Jenis,
            "Id_buku":self.__Id_buku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_Kode_Kategori(self, Kode_Kategori):
        url = self.__url+"?Kode_Kategori="+Kode_Kategori
        payload = {
            "Kode_Kategori":self.__Kode_Kategori,
            "Jenis":self.__Jenis,
            "Id_buku":self.__Id_buku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_Kode_Kategori(self,Kode_Kategori):
        url = self.__url+"?Kode_Kategori="+Kode_Kategori
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text