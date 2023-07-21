import requests
import json
class Prodi:
    def __init__(self):
        self.__id=None
        self.__kode_prodi = None
        self.__nama_prodi = None
        self.__url = "http://a0832601.xsph.ru/AppTugasBesar/prodi_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_prodi(self):
        return self.__kode_prodi
        
    @kode_prodi.setter
    def kode_prodi(self, value):
        self.__kode_prodi = value
    @property
    def nama_prodi(self):
        return self.__nama_prodi
        
    @nama_prodi.setter
    def nama_prodi(self, value):
        self.__nama_prodi = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_prodi(self, kode_prodi):
        url = self.__url+"?kode_prodi="+kode_prodi
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_prodi']
            self.__kode_prodi = item['kode_prodi']
            self.__nama_prodi = item['nama_prodi']
        return data
    def simpan(self):
        payload = {
            "kode_prodi":self.__kode_prodi,
            "nama_prodi":self.__nama_prodi
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_prodi(self, kode_prodi):
        url = self.__url+"?kode_prodi="+kode_prodi
        payload = {
            "kode_prodi":self.__kode_prodi,
            "nama_prodi":self.__nama_prodi
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_prodi(self,kode_prodi):
        url = self.__url+"?kode_prodi="+kode_prodi
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
