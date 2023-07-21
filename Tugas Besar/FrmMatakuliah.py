import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Matakuliah import *
class FrmMatakuliah:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("750x550")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='KODE_MATAKULIAH:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_MATAKULIAH:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='SKS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_matakuliah = Entry(mainFrame)
        self.txtKode_matakuliah.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_matakuliah.bind("<Return>", self.onCari)
        self.txtNama_matakuliah = Entry(mainFrame) 
        self.txtNama_matakuliah.grid(row=1, column=1, padx=5, pady=5)
        self.txtSks = Entry(mainFrame)
        self.txtSks.grid(row=2, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_matakuliah','kode_matakuliah','nama_matakuliah','sks')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_matakuliah', text='ID_MATAKULIAH')
        self.tree.column('id_matakuliah', width="150")
        self.tree.heading('kode_matakuliah', text='KODE_MATAKULIAH')
        self.tree.column('kode_matakuliah', width="150")
        self.tree.heading('nama_matakuliah', text='NAMA_MATAKULIAH')
        self.tree.column('nama_matakuliah', width="150")
        self.tree.heading('sks', text='SKS')
        self.tree.column('sks', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_matakuliah.delete(0,END)
        self.txtKode_matakuliah.insert(END,"")
        self.txtNama_matakuliah.delete(0,END)
        self.txtNama_matakuliah.insert(END,"")
        self.txtSks.delete(0,END)
        self.txtSks.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data matakuliah
        obj = Matakuliah()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_matakuliah"],d["kode_matakuliah"],d["nama_matakuliah"],d["sks"]))
    def onCari(self, event=None):
        kode_matakuliah = self.txtKode_matakuliah.get()
        obj = Matakuliah()
        a = obj.get_by_kode_matakuliah(kode_matakuliah)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_matakuliah = self.txtKode_matakuliah.get()
        obj = Matakuliah()
        res = obj.get_by_kode_matakuliah(kode_matakuliah)
        self.txtNama_matakuliah.delete(0,END)
        self.txtNama_matakuliah.insert(END,obj.nama_matakuliah)
        self.txtSks.delete(0,END)
        self.txtSks.insert(END,obj.sks)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_matakuliah = self.txtKode_matakuliah.get()
        nama_matakuliah = self.txtNama_matakuliah.get()
        sks = self.txtSks.get()
        # create new Object
        obj = Matakuliah()
        obj.kode_matakuliah = kode_matakuliah
        obj.nama_matakuliah = nama_matakuliah
        obj.sks = sks
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_matakuliah(kode_matakuliah)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_matakuliah = self.txtKode_matakuliah.get()
        obj = Matakuliah()
        obj.kode_matakuliah = kode_matakuliah
        if(self.ditemukan==True):
            res = obj.delete_by_kode_matakuliah(kode_matakuliah)
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
    aplikasi = FrmMatakuliah(root2, "Aplikasi Data Matakuliah")
    root2.mainloop()