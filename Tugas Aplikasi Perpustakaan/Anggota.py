import requests
import json
class Anggota:
    def __init__(self):
        self.__id=None
        self.__NIM = None
        self.__Nama = None
        self.__Jenis_kelamin = None
        self.__Alamat = None
        self.__No_telpon = None
        self.__url = "http://localhost/Perpustakaan/anggota_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def NIM(self):
        return self.__NIM
        
    @NIM.setter
    def NIM(self, value):
        self.__NIM = value
    @property
    def Nama(self):
        return self.__Nama
        
    @Nama.setter
    def Nama(self, value):
        self.__Nama = value
    @property
    def Jenis_kelamin(self):
        return self.__Jenis_kelamin
        
    @Jenis_kelamin.setter
    def Jenis_kelamin(self, value):
        self.__Jenis_kelamin = value
    @property
    def Alamat(self):
        return self.__Alamat
        
    @Alamat.setter
    def Alamat(self, value):
        self.__Alamat = value
    @property
    def No_telpon(self):
        return self.__No_telpon
        
    @No_telpon.setter
    def No_telpon(self, value):
        self.__No_telpon = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_NIM(self, NIM):
        url = self.__url+"?NIM="+NIM
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['Id_anggota']
            self.__NIM = item['NIM']
            self.__Nama = item['Nama']
            self.__Jenis_kelamin = item['Jenis_kelamin']
            self.__Alamat = item['Alamat']
            self.__No_telpon = item['No_telpon']
        return data
    def simpan(self):
        payload = {
            "NIM":self.__NIM,
            "Nama":self.__Nama,
            "Jenis_kelamin":self.__Jenis_kelamin,
            "Alamat":self.__Alamat,
            "No_telpon":self.__No_telpon
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_NIM(self, NIM):
        url = self.__url+"?NIM="+NIM
        payload = {
            "NIM":self.__NIM,
            "Nama":self.__Nama,
            "Jenis_kelamin":self.__Jenis_kelamin,
            "Alamat":self.__Alamat,
            "No_telpon":self.__No_telpon
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_NIM(self,NIM):
        url = self.__url+"?NIM="+NIM
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
