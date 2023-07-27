import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__NIM = None
        self.__Tanggal_pinjam = None
        self.__Tanggal_kembali = None
        self.__Id_buku = None
        self.__Id_petugas = None
        self.__Id_anggota = None
        self.__url = "http://localhost/Perpustakaan/peminjaman_api.php"
                    
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
    def Tanggal_pinjam(self):
        return self.__Tanggal_pinjam
        
    @Tanggal_pinjam.setter
    def Tanggal_pinjam(self, value):
        self.__Tanggal_pinjam = value
    @property
    def Tanggal_kembali(self):
        return self.__Tanggal_kembali
        
    @Tanggal_kembali.setter
    def Tanggal_kembali(self, value):
        self.__Tanggal_kembali = value
    @property
    def Id_buku(self):
        return self.__Id_buku
        
    @Id_buku.setter
    def Id_buku(self, value):
        self.__Id_buku = value
    @property
    def Id_petugas(self):
        return self.__Id_petugas
        
    @Id_petugas.setter
    def Id_petugas(self, value):
        self.__Id_petugas = value
    @property
    def Id_anggota(self):
        return self.__Id_anggota
        
    @Id_anggota.setter
    def Id_anggota(self, value):
        self.__Id_anggota = value
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
            self.__id = item['Id_peminjaman']
            self.__NIM = item['NIM']
            self.__Tanggal_pinjam = item['Tanggal_pinjam']
            self.__Tanggal_kembali = item['Tanggal_kembali']
            self.__Id_buku = item['Id_buku']
            self.__Id_petugas = item['Id_petugas']
            self.__Id_anggota = item['Id_anggota']
        return data
    def simpan(self):
        payload = {
            "NIM":self.__NIM,
            "Tanggal_pinjam":self.__Tanggal_pinjam,
            "Tanggal_kembali":self.__Tanggal_kembali,
            "Id_buku":self.__Id_buku,
            "Id_petugas":self.__Id_petugas,
            "Id_anggota":self.__Id_anggota
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_NIM(self, NIM):
        url = self.__url+"?NIM="+NIM
        payload = {
            "NIM":self.__NIM,
            "Tanggal_pinjam":self.__Tanggal_pinjam,
            "Tanggal_kembali":self.__Tanggal_kembali,
            "Id_buku":self.__Id_buku,
            "Id_petugas":self.__Id_petugas,
            "Id_anggota":self.__Id_anggota
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
