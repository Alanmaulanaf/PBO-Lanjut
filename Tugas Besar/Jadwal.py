import requests
import json
class Jadwal:
    def __init__(self):
        self.__id=None
        self.__kode_jadwal = None
        self.__matakuliah = None
        self.__dosen = None
        self.__kelas = None
        self.__ruang = None
        self.__prodi = None
        self.__hari = None
        self.__jam_mulai = None
        self.__jam_selesai = None
        self.__url = "http://a0832601.xsph.ru/AppTugasBesar/jadwal_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def kode_jadwal(self):
        return self.__kode_jadwal
        
    @kode_jadwal.setter
    def kode_jadwal(self, value):
        self.__kode_jadwal = value
    @property
    def matakuliah(self):
        return self.__matakuliah
        
    @matakuliah.setter
    def matakuliah(self, value):
        self.__matakuliah = value
    @property
    def dosen(self):
        return self.__dosen
        
    @dosen.setter
    def dosen(self, value):
        self.__dosen = value
    @property
    def kelas(self):
        return self.__kelas
        
    @kelas.setter
    def kelas(self, value):
        self.__kelas = value
    @property
    def ruang(self):
        return self.__ruang
        
    @ruang.setter
    def ruang(self, value):
        self.__ruang = value
    @property
    def prodi(self):
        return self.__prodi
        
    @prodi.setter
    def prodi(self, value):
        self.__prodi = value
    @property
    def hari(self):
        return self.__hari
        
    @hari.setter
    def hari(self, value):
        self.__hari = value
    @property
    def jam_mulai(self):
        return self.__jam_mulai
        
    @jam_mulai.setter
    def jam_mulai(self, value):
        self.__jam_mulai = value
    @property
    def jam_selesai(self):
        return self.__jam_selesai
        
    @jam_selesai.setter
    def jam_selesai(self, value):
        self.__jam_selesai = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_kode_jadwal(self, kode_jadwal):
        url = self.__url+"?kode_jadwal="+kode_jadwal
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id_jadwal']
            self.__kode_jadwal = item['kode_jadwal']
            self.__matakuliah = item['matakuliah']
            self.__dosen = item['dosen']
            self.__kelas = item['kelas']
            self.__ruang = item['ruang']
            self.__prodi = item['prodi']
            self.__hari = item['hari']
            self.__jam_mulai = item['jam_mulai']
            self.__jam_selesai = item['jam_selesai']
        return data
    def simpan(self):
        payload = {
            "kode_jadwal":self.__kode_jadwal,
            "matakuliah":self.__matakuliah,
            "dosen":self.__dosen,
            "kelas":self.__kelas,
            "ruang":self.__ruang,
            "prodi":self.__prodi,
            "hari":self.__hari,
            "jam_mulai":self.__jam_mulai,
            "jam_selesai":self.__jam_selesai
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_kode_jadwal(self, kode_jadwal):
        url = self.__url+"?kode_jadwal="+kode_jadwal
        payload = {
            "kode_jadwal":self.__kode_jadwal,
            "matakuliah":self.__matakuliah,
            "dosen":self.__dosen,
            "kelas":self.__kelas,
            "ruang":self.__ruang,
            "prodi":self.__prodi,
            "hari":self.__hari,
            "jam_mulai":self.__jam_mulai,
            "jam_selesai":self.__jam_selesai
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_kode_jadwal(self,kode_jadwal):
        url = self.__url+"?kode_jadwal="+kode_jadwal
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
