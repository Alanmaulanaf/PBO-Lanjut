import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Petugas import *
class FrmPetugas:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("650x550")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='NIP:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JABATAN:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNIP = Entry(mainFrame) 
        self.txtNIP.grid(row=0, column=1, padx=5, pady=5)
        self.txtNIP.bind("<Return>",self.onCari)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtJabatan = Entry(mainFrame) 
        self.txtJabatan.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=3, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, fg='black', bg='yellow')
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, bg='gold', fg='red')
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, fg='blue', bg='black')
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('Id_petugas','NIP','Nama','Jabatan','Alamat')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('Id_petugas', text='ID_PETUGAS')
        self.tree.column('Id_petugas', width="130")
        self.tree.heading('NIP', text='NIP')
        self.tree.column('NIP', width="130")
        self.tree.heading('Nama', text='NAMA')
        self.tree.column('Nama', width="130")
        self.tree.heading('Jabatan', text='JABATAN')
        self.tree.column('Jabatan', width="130")
        self.tree.heading('Alamat', text='ALAMAT')
        self.tree.column('Alamat', width="130")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNIP.delete(0,END)
        self.txtNIP.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJabatan.delete(0,END)
        self.txtJabatan.insert(END,"")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data petugas
        obj = Petugas()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["Id_petugas"],d["NIP"],d["Nama"],d["Jabatan"],d["Alamat"]))
    def onCari(self, event=None):
        NIP = self.txtNIP.get()
        obj = Petugas()
        a = obj.get_by_NIP(NIP)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        NIP = self.txtNIP.get()
        obj = Petugas()
        res = obj.get_by_NIP(NIP)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.Nama)
        self.txtJabatan.delete(0,END)
        self.txtJabatan.insert(END,obj.Jabatan)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.Alamat)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        NIP = self.txtNIP.get()
        Nama = self.txtNama.get()
        Jabatan = self.txtJabatan.get()
        Alamat = self.txtAlamat.get()
        # create new Object
        obj = Petugas()
        obj.NIP = NIP
        obj.Nama = Nama
        obj.Jabatan = Jabatan
        obj.Alamat = Alamat
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_NIP(NIP)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        NIP = self.txtNIP.get()
        obj = Petugas()
        obj.NIP = NIP
        if(self.ditemukan==True):
            res = obj.delete_by_NIP(NIP)
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
    aplikasi = FrmPetugas(root2, "Aplikasi Data Petugas")
    root2.mainloop()
