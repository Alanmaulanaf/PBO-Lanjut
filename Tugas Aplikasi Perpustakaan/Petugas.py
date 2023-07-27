import requests
import json
class Petugas:
    def __init__(self):
        self.__id=None
        self.__NIP = None
        self.__Nama = None
        self.__Jabatan = None
        self.__Alamat = None
        self.__url = "http://localhost/Perpustakaan/petugas_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def NIP(self):
        return self.__NIP
        
    @NIP.setter
    def NIP(self, value):
        self.__NIP = value
    @property
    def Nama(self):
        return self.__Nama
        
    @Nama.setter
    def Nama(self, value):
        self.__Nama = value
    @property
    def Jabatan(self):
        return self.__Jabatan
        
    @Jabatan.setter
    def Jabatan(self, value):
        self.__Jabatan = value
    @property
    def Alamat(self):
        return self.__Alamat
        
    @Alamat.setter
    def Alamat(self, value):
        self.__Alamat = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_NIP(self, NIP):
        url = self.__url+"?NIP="+NIP
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['Id_petugas']
            self.__NIP = item['NIP']
            self.__Nama = item['Nama']
            self.__Jabatan = item['Jabatan']
            self.__Alamat = item['Alamat']
        return data
    def simpan(self):
        payload = {
            "NIP":self.__NIP,
            "Nama":self.__Nama,
            "Jabatan":self.__Jabatan,
            "Alamat":self.__Alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_NIP(self, NIP):
        url = self.__url+"?NIP="+NIP
        payload = {
            "NIP":self.__NIP,
            "Nama":self.__Nama,
            "Jabatan":self.__Jabatan,
            "Alamat":self.__Alamat
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_NIP(self,NIP):
        url = self.__url+"?NIP="+NIP
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text