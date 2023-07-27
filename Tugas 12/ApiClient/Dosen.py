import requests
import json
class Dosen:
    def __init__(self):
        self.__id=None
        self.__nidn = None
        self.__nama = None
        self.__jk = None
        self.__prodi = None
        self.__jabatan = None
        self.__url = "http://localhost/appakademik/dosen_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def nidn(self):
        return self.__nidn
        
    @nidn.setter
    def nidn(self, value):
        self.__nidn = value
    @property
    def nama(self):
        return self.__nama
        
    @nama.setter
    def nama(self, value):
        self.__nama = value
    @property
    def jk(self):
        return self.__jk
        
    @jk.setter
    def jk(self, value):
        self.__jk = value
    @property
    def prodi(self):
        return self.__prodi
        
    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
    @property
    def jabatan(self):
        return self.__jabatan
        
    @jabatan.setter
    def jabatan(self, value):
        self.__jabatan = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_nidn(self, nidn):
        url = self.__url+"?nidn="+nidn
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['nid']
            self.__nidn = item['nidn']
            self.__nama = item['nama']
            self.__jk = item['jk']
            self.__prodi = item['prodi']
            self.__jabatan = item['jabatan']
        return data
    def simpan(self):
        payload = {
            "nidn":self.__nidn,
            "nama":self.__nama,
            "jk":self.__jk,
            "prodi":self.__prodi,
            "jabatan":self.__jabatan
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_nidn(self, nidn):
        url = self.__url+"?nidn="+nidn
        payload = {
            "nidn":self.__nidn,
            "nama":self.__nama,
            "jk":self.__jk,
            "prodi":self.__prodi,
            "jabatan":self.__jabatan
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_nidn(self,nidn):
        url = self.__url+"?nidn="+nidn
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text