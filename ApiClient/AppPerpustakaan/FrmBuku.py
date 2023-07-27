import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Buku import *
class FrmBuku:
    
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
        Label(mainFrame, text='KODE_BUKU:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUDUL:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENULIS:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PENERBIT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TAHUN_TERBIT:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='STOK:').grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_buku = Entry(mainFrame) 
        self.txtKode_buku.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_buku.bind("<Return>",self.onCari)
        self.txtJudul = Entry(mainFrame) 
        self.txtJudul.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenulis = Entry(mainFrame) 
        self.txtPenulis.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtPenerbit = Entry(mainFrame) 
        self.txtPenerbit.grid(row=3, column=1, padx=5, pady=5)
        self.txtTahun_terbit = Entry(mainFrame) 
        self.txtTahun_terbit.grid(row=4, column=1, padx=5, pady=5)
        self.txtStok = Entry(mainFrame) 
        self.txtStok.grid(row=5, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, bg='orange', fg='green')
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, bg='red', fg='yellow')
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, bg='pink', fg='black')
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('Id_buku','Kode_buku','Judul','Penulis','Penerbit','Tahun_terbit','Stok')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('Id_buku', text='ID_BUKU')
        self.tree.column('Id_buku', width="90")
        self.tree.heading('Kode_buku', text='KODE_BUKU')
        self.tree.column('Kode_buku', width="90")
        self.tree.heading('Judul', text='JUDUL')
        self.tree.column('Judul', width="100")
        self.tree.heading('Penulis', text='PENULIS')
        self.tree.column('Penulis', width="90")
        self.tree.heading('Penerbit', text='PENERBIT')
        self.tree.column('Penerbit', width="90")
        self.tree.heading('Tahun_terbit', text='TAHUN_TERBIT')
        self.tree.column('Tahun_terbit', width="90")
        self.tree.heading('Stok', text='STOK')
        self.tree.column('Stok', width="90")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_buku.delete(0,END)
        self.txtKode_buku.insert(END,"")
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,"")
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,"")
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,"")
        self.txtTahun_terbit.delete(0,END)
        self.txtTahun_terbit.insert(END,"")
        self.txtStok.delete(0,END)
        self.txtStok.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data buku
        obj = Buku()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["Id_buku"],d["Kode_buku"],d["Judul"],d["Penulis"],d["Penerbit"],d["Tahun_terbit"],d["Stok"]))
    def onCari(self, event=None):
        Kode_buku = self.txtKode_buku.get()
        obj = Buku()
        a = obj.get_by_Kode_buku(Kode_buku)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        Kode_buku = self.txtKode_buku.get()
        obj = Buku()
        res = obj.get_by_Kode_buku(Kode_buku)
        self.txtJudul.delete(0,END)
        self.txtJudul.insert(END,obj.Judul)
        self.txtPenulis.delete(0,END)
        self.txtPenulis.insert(END,obj.Penulis)
        self.txtPenerbit.delete(0,END)
        self.txtPenerbit.insert(END,obj.Penerbit)
        self.txtTahun_terbit.delete(0,END)
        self.txtTahun_terbit.insert(END,obj.Tahun_terbit)
        self.txtStok.delete(0,END)
        self.txtStok.insert(END,obj.Stok)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        Kode_buku = self.txtKode_buku.get()
        Judul = self.txtJudul.get()
        Penulis = self.txtPenulis.get()
        Penerbit = self.txtPenerbit.get()
        Tahun_terbit = self.txtTahun_terbit.get()
        Stok = self.txtStok.get()
        # create new Object
        obj = Buku()
        obj.Kode_buku = Kode_buku
        obj.Judul = Judul
        obj.Penulis = Penulis
        obj.Penerbit = Penerbit
        obj.Tahun_terbit = Tahun_terbit
        obj.Stok = Stok
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_Kode_buku(Kode_buku)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        Kode_buku = self.txtKode_buku.get()
        obj = Buku()
        obj.Kode_buku = Kode_buku
        if(self.ditemukan==True):
            res = obj.delete_by_Kode_buku(Kode_buku)
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
    aplikasi = FrmBuku(root2, "Aplikasi Data Buku")
    root2.mainloop()