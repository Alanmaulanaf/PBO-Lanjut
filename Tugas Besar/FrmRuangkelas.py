import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Ruangkelas import *
class FrmRuangkelas:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_RUANG:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_RUANG:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtKode_ruang = Entry(mainFrame)
        self.txtKode_ruang.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_ruang.bind("<Return>", self.onCari)
        self.txtNama_ruang = Entry(mainFrame)
        self.txtNama_ruang.grid(row=1, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_ruang','kode_ruang','nama_ruang')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_ruang', text='ID_RUANG')
        self.tree.column('id_ruang', width="100")
        self.tree.heading('kode_ruang', text='KODE_RUANG')
        self.tree.column('kode_ruang', width="100")
        self.tree.heading('nama_ruang', text='NAMA_RUANG')
        self.tree.column('nama_ruang', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.btnSimpan.config(text="Simpan")
        self.txtKode_ruang.delete(0,END)
        self.txtKode_ruang.insert(END,"")
        self.txtNama_ruang.delete(0,END)
        self.txtNama_ruang.insert(END,"")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data ruangkelas
        obj = Ruangkelas()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_ruang"],d["kode_ruang"],d["nama_ruang"]))
    def onCari(self, event=None):
        kode_ruang = self.txtKode_ruang.get()
        obj = Ruangkelas()
        a = obj.get_by_kode_ruang(kode_ruang)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_ruang = self.txtKode_ruang.get()
        obj = Ruangkelas()
        res = obj.get_by_kode_ruang(kode_ruang)
        self.txtNama_ruang.delete(0,END)
        self.txtNama_ruang.insert(END,obj.nama_ruang)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_ruang = self.txtKode_ruang.get()
        nama_ruang = self.txtNama_ruang.get()
        # create new Object
        obj = Ruangkelas()
        obj.kode_ruang = kode_ruang
        obj.nama_ruang = nama_ruang
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_ruang(kode_ruang)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_ruang = self.txtKode_ruang.get()
        obj = Ruangkelas()
        obj.kode_ruang = kode_ruang
        if(self.ditemukan==True):
            res = obj.delete_by_kode_ruang(kode_ruang)
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
    aplikasi = FrmRuangkelas(root2, "Aplikasi Data Ruangkelas")
    root2.mainloop()