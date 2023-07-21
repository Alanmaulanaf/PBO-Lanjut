import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Prodi import *
class FrmProdi:
    
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
        Label(mainFrame, text='KODE_PRODI:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_PRODI:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_prodi = Entry(mainFrame) 
        self.txtKode_prodi.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_prodi.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama_prodi = Entry(mainFrame) 
        self.txtNama_prodi.grid(row=1, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_prodi','kode_prodi','nama_prodi')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_prodi', text='ID_PRODI')
        self.tree.column('id_prodi', width="100")
        self.tree.heading('kode_prodi', text='KODE_PRODI')
        self.tree.column('kode_prodi', width="100")
        self.tree.heading('nama_prodi', text='NAMA_PRODI')
        self.tree.column('nama_prodi', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_prodi.delete(0,END)
        self.txtKode_prodi.insert(END,"")
        self.txtNama_prodi.delete(0,END)
        self.txtNama_prodi.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data prodi
        obj = Prodi()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_prodi"],d["kode_prodi"],d["nama_prodi"]))
    def onCari(self, event=None):
        kode_prodi = self.txtKode_prodi.get()
        obj = Prodi()
        a = obj.get_by_kode_prodi(kode_prodi)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_prodi = self.txtKode_prodi.get()
        obj = Prodi()
        res = obj.get_by_kode_prodi(kode_prodi)
        self.txtKode_prodi.delete(0,END)
        self.txtKode_prodi.insert(END,obj.kode_prodi)
        self.txtNama_prodi.delete(0,END)
        self.txtNama_prodi.insert(END,obj.nama_prodi)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_prodi = self.txtKode_prodi.get()
        nama_prodi = self.txtNama_prodi.get()
        # create new Object
        obj = Prodi()
        obj.kode_prodi = kode_prodi
        obj.nama_prodi = nama_prodi
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_prodi(kode_prodi)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_prodi = self.txtKode_prodi.get()
        obj = Prodi()
        obj.kode_prodi = kode_prodi
        if(self.ditemukan==True):
            res = obj.delete_by_kode_prodi(kode_prodi)
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
    aplikasi = FrmProdi(root2, "Aplikasi Data Prodi")
    root2.mainloop()