import requests
import json
class Ruangkelas:
    def __init__(self):
        self.__id=None
        self.__kode_ruang = None
        self.__nama_ruang = None
        self.__url = "http://a0832601.xsph.ru/AppTugasBesar/ruangkelas_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_ruang(self):
        return self.__kode_ruang
        
    @kode_ruang.setter
    def kode_ruang(self, value):
        self.__kode_ruang = value
    @property
    def nama_ruang(self):
        return self.__nama_ruang
        
    @nama_ruang.setter
    def nama_ruang(self, value):
        self.__nama_ruang = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_ruang(self, kode_ruang):
        url = self.__url+"?kode_ruang="+kode_ruang
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_ruang']
            self.__kode_ruang = item['kode_ruang']
            self.__nama_ruang = item['nama_ruang']
        return data
    def simpan(self):
        payload = {
            "kode_ruang":self.__kode_ruang,
            "nama_ruang":self.__nama_ruang
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_ruang(self, kode_ruang):
        url = self.__url+"?kode_ruang="+kode_ruang
        payload = {
            "kode_ruang":self.__kode_ruang,
            "nama_ruang":self.__nama_ruang
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_ruang(self,kode_ruang):
        url = self.__url+"?kode_ruang="+kode_ruang
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
