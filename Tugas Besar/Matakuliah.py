import requests
import json
class Matakuliah:
    def __init__(self):
        self.__id=None
        self.__kode_matakuliah = None
        self.__nama_matakuliah = None
        self.__sks = None
        self.__url = "http://a0832601.xsph.ru/AppTugasBesar/matakuliah_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_matakuliah(self):
        return self.__kode_matakuliah
        
    @kode_matakuliah.setter
    def kode_matakuliah(self, value):
        self.__kode_matakuliah = value
    @property
    def nama_matakuliah(self):
        return self.__nama_matakuliah
        
    @nama_matakuliah.setter
    def nama_matakuliah(self, value):
        self.__nama_matakuliah = value
    @property
    def sks(self):
        return self.__sks
        
    @sks.setter
    def sks(self, value):
        self.__sks = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_matakuliah(self, kode_matakuliah):
        url = self.__url+"?kode_matakuliah="+kode_matakuliah
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_matakuliah']
            self.__kode_matakuliah = item['kode_matakuliah']
            self.__nama_matakuliah = item['nama_matakuliah']
            self.__sks = item['sks']
        return data
    def simpan(self):
        payload = {
            "kode_matakuliah":self.__kode_matakuliah,
            "nama_matakuliah":self.__nama_matakuliah,
            "sks":self.__sks
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_matakuliah(self, kode_matakuliah):
        url = self.__url+"?kode_matakuliah="+kode_matakuliah
        payload = {
            "kode_matakuliah":self.__kode_matakuliah,
            "nama_matakuliah":self.__nama_matakuliah,
            "sks":self.__sks
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_matakuliah(self,kode_matakuliah):
        url = self.__url+"?kode_matakuliah="+kode_matakuliah
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text