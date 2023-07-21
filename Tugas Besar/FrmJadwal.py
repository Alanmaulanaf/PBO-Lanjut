import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Jadwal import *
class FrmJadwal:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("1150x950")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_JADWAL:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='MATAKULIAH:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='DOSEN:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KELAS:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='RUANG:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PRODI:').grid(row=1, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='HARI:').grid(row=2, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JAM_MULAI:').grid(row=3, column=2,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JAM_SELESAI:').grid(row=4, column=2,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_jadwal = Entry(mainFrame)
        self.txtKode_jadwal.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_jadwal.bind("<Return>", self.onCari)
        self.txtMatakuliah = Entry(mainFrame) 
        self.txtMatakuliah.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtDosen = Entry(mainFrame) 
        self.txtDosen.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtKelas = Entry(mainFrame) 
        self.txtKelas.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtRuang = Entry(mainFrame) 
        self.txtRuang.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtProdi = Entry(mainFrame) 
        self.txtProdi.grid(row=1, column=3, padx=5, pady=5)
        # Textbox
        self.txtHari = Entry(mainFrame) 
        self.txtHari.grid(row=2, column=3, padx=5, pady=5)
        self.txtJam_mulai = Entry(mainFrame)
        self.txtJam_mulai.grid(row=3, column=3, padx=5, pady=5)
        self.txtJam_selesai = Entry(mainFrame)
        self.txtJam_selesai.grid(row=4, column=3, padx=5, pady=5)
        # Button
        self.btnCari = Button(mainFrame, text='Cari', command=self.onCari, width=10, bg='blue', fg='yellow')
        self.btnCari.grid(row=0, column=2, padx=5, pady=5)
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, fg='red', bg='yellow')
        self.btnSimpan.grid(row=5, column=1, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, fg='green', bg='brown')
        self.btnClear.grid(row=5, column=2, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, fg='gold', bg='white')
        self.btnHapus.grid(row=5, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_jadwal','kode_jadwal','matakuliah','dosen','kelas','ruang','prodi','hari','jam_mulai','jam_selesai')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_jadwal', text='ID_JADWAL')
        self.tree.column('id_jadwal', width="100")
        self.tree.heading('kode_jadwal', text='KODE_JADWAL')
        self.tree.column('kode_jadwal', width="100")
        self.tree.heading('matakuliah', text='MATAKULIAH')
        self.tree.column('matakuliah', width="100")
        self.tree.heading('dosen', text='DOSEN')
        self.tree.column('dosen', width="100")
        self.tree.heading('kelas', text='KELAS')
        self.tree.column('kelas', width="100")
        self.tree.heading('ruang', text='RUANG')
        self.tree.column('ruang', width="100")
        self.tree.heading('prodi', text='PRODI')
        self.tree.column('prodi', width="100")
        self.tree.heading('hari', text='HARI')
        self.tree.column('hari', width="100")
        self.tree.heading('jam_mulai', text='JAM_MULAI')
        self.tree.column('jam_mulai', width="100")
        self.tree.heading('jam_selesai', text='JAM_SELESAI')
        self.tree.column('jam_selesai', width="100")
        # set tree position
        self.tree.place(x=0, y=250)
        
    def onClear(self, event=None):
        self.txtKode_jadwal.delete(0,END)
        self.txtKode_jadwal.insert(END,"")
        self.txtMatakuliah.delete(0,END)
        self.txtMatakuliah.insert(END,"")
        self.txtDosen.delete(0,END)
        self.txtDosen.insert(END,"")
        self.txtKelas.delete(0,END)
        self.txtKelas.insert(END,"")
        self.txtRuang.delete(0,END)
        self.txtRuang.insert(END,"")
        self.txtProdi.delete(0,END)
        self.txtProdi.insert(END,"")
        self.txtHari.delete(0,END)
        self.txtHari.insert(END,"")
        self.txtJam_mulai.delete(0,END)
        self.txtJam_mulai.insert(END,"")
        self.txtJam_selesai.delete(0,END)
        self.txtJam_selesai.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data jadwal
        obj = Jadwal()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_jadwal"],d["kode_jadwal"],d["matakuliah"],d["dosen"],d["kelas"],d["ruang"],d["prodi"],d["hari"],d["jam_mulai"],d["jam_selesai"]))
    def onCari(self, event=None):
        kode_jadwal = self.txtKode_jadwal.get()
        obj = Jadwal()
        a = obj.get_by_kode_jadwal(kode_jadwal)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_jadwal = self.txtKode_jadwal.get()
        obj = Jadwal()
        res = obj.get_by_kode_jadwal(kode_jadwal)
        self.txtMatakuliah.delete(0,END)
        self.txtMatakuliah.insert(END,obj.matakuliah)
        self.txtDosen.delete(0,END)
        self.txtDosen.insert(END,obj.dosen)
        self.txtKelas.delete(0,END)
        self.txtKelas.insert(END,obj.kelas)
        self.txtRuang.delete(0,END)
        self.txtRuang.insert(END,obj.ruang)
        self.txtProdi.delete(0,END)
        self.txtProdi.insert(END,obj.prodi)
        self.txtHari.delete(0,END)
        self.txtHari.insert(END,obj.hari)
        self.txtJam_mulai.delete(0,END)
        self.txtJam_mulai.insert(END,obj.jam_mulai)
        self.txtJam_selesai.delete(0,END)
        self.txtJam_selesai.insert(END,obj.jam_selesai)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_jadwal = self.txtKode_jadwal.get()
        matakuliah = self.txtMatakuliah.get()
        dosen = self.txtDosen.get()
        kelas = self.txtKelas.get()
        ruang = self.txtRuang.get()
        prodi = self.txtProdi.get()
        hari = self.txtHari.get()
        jam_mulai = self.txtJam_mulai.get()
        jam_selesai = self.txtJam_selesai.get()
        # create new Object
        obj = Jadwal()
        obj.kode_jadwal = kode_jadwal
        obj.matakuliah = matakuliah
        obj.dosen = dosen
        obj.kelas = kelas
        obj.ruang = ruang
        obj.prodi = prodi
        obj.hari = hari
        obj.jam_mulai = jam_mulai
        obj.jam_selesai = jam_selesai
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_jadwal(kode_jadwal)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_jadwal = self.txtKode_jadwal.get()
        obj = Jadwal()
        obj.kode_jadwal = kode_jadwal
        if(self.ditemukan==True):
            res = obj.delete_by_kode_jadwal(kode_jadwal)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmJadwal(root2, "Aplikasi Data Jadwal")
    root2.mainloop()