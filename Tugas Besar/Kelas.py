import requests
import json
class Kelas:
    def __init__(self):
        self.__id=None
        self.__kode_kelas = None
        self.__nama_kelas = None
        self.__semester = None
        self.__url = "http://a0832601.xsph.ru/AppTugasBesar/kelas_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_kelas(self):
        return self.__kode_kelas
        
    @kode_kelas.setter
    def kode_kelas(self, value):
        self.__kode_kelas = value
    @property
    def nama_kelas(self):
        return self.__nama_kelas
        
    @nama_kelas.setter
    def nama_kelas(self, value):
        self.__nama_kelas = value
    @property
    def semester(self):
        return self.__semester
        
    @semester.setter
    def semester(self, value):
        self.__semester = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_kelas(self, kode_kelas):
        url = self.__url+"?kode_kelas="+kode_kelas
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_kelas']
            self.__kode_kelas = item['kode_kelas']
            self.__nama_kelas = item['nama_kelas']
            self.__semester = item['semester']
        return data
    def simpan(self):
        payload = {
            "kode_kelas":self.__kode_kelas,
            "nama_kelas":self.__nama_kelas,
            "semester":self.__semester
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_kelas(self, kode_kelas):
        url = self.__url+"?kode_kelas="+kode_kelas
        payload = {
            "kode_kelas":self.__kode_kelas,
            "nama_kelas":self.__nama_kelas,
            "semester":self.__semester
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_kelas(self,kode_kelas):
        url = self.__url+"?kode_kelas="+kode_kelas
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
