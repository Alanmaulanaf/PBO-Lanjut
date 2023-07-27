import requests
import json
class Dokter:
    def __init__(self):
        self.__id=None
        self.__Nip = None
        self.__Nama = None
        self.__JenisKelamin = None
        self.__Spesialis = None
        self.__url = "http://localhost/appdokter/dokter_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def Nip(self):
        return self.__Nip
        
    @Nip.setter
    def Nip(self, value):
        self.__Nip = value
    @property
    def Nama(self):
        return self.__Nama
        
    @Nama.setter
    def Nama(self, value):
        self.__Nama = value
    @property
    def JenisKelamin(self):
        return self.__JenisKelamin
        
    @JenisKelamin.setter
    def JenisKelamin(self, value):
        self.__JenisKelamin = value
    @property
    def Spesialis(self):
        return self.__Spesialis
        
    @Spesialis.setter
    def Spesialis(self, value):
        self.__Spesialis = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_Nip(self, Nip):
        url = self.__url+"?Nip="+Nip
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['iddokter']
            self.__Nip = item['Nip']
            self.__Nama = item['Nama']
            self.__JenisKelamin = item['JenisKelamin']
            self.__Spesialis = item['Spesialis']
        return data
    def simpan(self):
        payload = {
            "Nip":self.__Nip,
            "Nama":self.__Nama,
            "JenisKelamin":self.__JenisKelamin,
            "Spesialis":self.__Spesialis
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_Nip(self, Nip):
        url = self.__url+"?Nip="+Nip
        payload = {
            "Nip":self.__Nip,
            "Nama":self.__Nama,
            "JenisKelamin":self.__JenisKelamin,
            "Spesialis":self.__Spesialis
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_Nip(self,Nip):
        url = self.__url+"?Nip="+Nip
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
