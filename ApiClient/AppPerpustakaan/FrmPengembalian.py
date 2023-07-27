import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Pengembalian import *
class FrmPengembalian:
    
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
        Label(mainFrame, text='NIM:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL_PENGEMBALIAN:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STATUS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='DENDA:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_ANGGOTA:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_PETUGAS:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_BUKU:').grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNIM = Entry(mainFrame)
        self.txtNIM.grid(row=0, column= 1, padx=5, pady=5)
        self.txtNIM.bind("<Return>",self.onCari)
        
        self.txtTanggal_pengembalian = Entry(mainFrame)
        self.txtTanggal_pengembalian.grid(row=1, column=1, padx=5, pady=5)

        self.txtStatus = Entry(mainFrame) 
        self.txtStatus.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtDenda = Entry(mainFrame) 
        self.txtDenda.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_anggota = Entry(mainFrame) 
        self.txtId_anggota.grid(row=4, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_petugas = Entry(mainFrame) 
        self.txtId_petugas.grid(row=5, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_buku = Entry(mainFrame) 
        self.txtId_buku.grid(row=6, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, fg='red', bg='green')
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, bg='white', fg='blue')
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, bg='black', fg='red')
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('Id_pengembalian','NIM','Tanggal_pengembalian','Status','Denda','Id_anggota','Id_petugas','Id_buku')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('Id_pengembalian', text='ID_PENGEMBALIAN')
        self.tree.column('Id_pengembalian', width="50")
        self.tree.heading('NIM', text='NIM')
        self.tree.column('NIM', width="70")
        self.tree.heading('Tanggal_pengembalian', text='TANGGAL_PENGEMBALIAN')
        self.tree.column('Tanggal_pengembalian', width="100")
        self.tree.heading('Status', text='STATUS')
        self.tree.column('Status', width="80")
        self.tree.heading('Denda', text='DENDA')
        self.tree.column('Denda', width="90")
        self.tree.heading('Id_anggota', text='ID_ANGGOTA')
        self.tree.column('Id_anggota', width="90")
        self.tree.heading('Id_petugas', text='ID_PETUGAS')
        self.tree.column('Id_petugas', width="90")
        self.tree.heading('Id_buku', text='ID_BUKU')
        self.tree.column('Id_buku', width="90")
        # set tree position
        self.tree.place(x=0, y=250)
        
    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
        self.txtTanggal_pengembalian.delete(0,END)
        self.txtTanggal_pengembalian.insert(END,"")
        self.txtStatus.delete(0,END)
        self.txtStatus.insert(END,"")
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,"")
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,"")
        self.txtId_petugas.delete(0,END)
        self.txtId_petugas.insert(END,"")
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data pengembalian
        obj = Pengembalian()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["Id_pengembalian"],d["NIM"],d["Tanggal_pengembalian"],d["Status"],d["Denda"],d["Id_anggota"],d["Id_petugas"],d["Id_buku"]))
    def onCari(self, event=None):
        NIM = self.txtNIM.get()
        obj = Pengembalian()
        a = obj.get_by_NIM(NIM)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
            messagebox.showinfo("Info", "Data Ditemukan")
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        NIM = self.txtNIM.get()
        obj = Pengembalian()
        res = obj.get_by_NIM(NIM)
        self.txtTanggal_pengembalian.delete(0,END)
        self.txtTanggal_pengembalian.insert(END,obj.Tanggal_pengembalian)
        self.txtStatus.delete(0,END)
        self.txtStatus.insert(END,obj.Status)
        self.txtDenda.delete(0,END)
        self.txtDenda.insert(END,obj.Denda)
        self.txtId_anggota.delete(0,END)
        self.txtId_anggota.insert(END,obj.Id_anggota)
        self.txtId_petugas.delete(0,END)
        self.txtId_petugas.insert(END,obj.Id_petugas)
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,obj.Id_buku)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        NIM = self.txtNIM.get()
        Tanggal_pengembalian = self.txtTanggal_pengembalian.get()
        Status = self.txtStatus.get()
        Denda = self.txtDenda.get()
        Id_anggota = self.txtId_anggota.get()
        Id_petugas = self.txtId_petugas.get()
        Id_buku = self.txtId_buku.get()
        # create new Object
        obj = Pengembalian()
        obj.NIM = NIM
        obj.Tanggal_pengembalian = Tanggal_pengembalian
        obj.Status = Status
        obj.Denda = Denda
        obj.Id_anggota = Id_anggota
        obj.Id_petugas = Id_petugas
        obj.Id_buku = Id_buku
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_NIM(NIM)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        NIM = self.txtNIM.get()
        obj = Pengembalian()
        obj.NIM = NIM
        if(self.ditemukan==True):
            res = obj.delete_by_NIM(NIM)
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
    aplikasi = FrmPengembalian(root2, "Aplikasi Data Pengembalian")
    root2.mainloop()