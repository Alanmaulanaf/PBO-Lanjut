import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Kategori import *
class FrmKategori:
    
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
        Label(mainFrame, text='KODE_KATEGORI:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JENIS:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ID_BUKU:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_Kategori = Entry(mainFrame) 
        self.txtKode_Kategori.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_Kategori.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtJenis = Entry(mainFrame) 
        self.txtJenis.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtId_buku = Entry(mainFrame) 
        self.txtId_buku.grid(row=2, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, fg='black', bg='blue')
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, fg='white', bg='gold')
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, fg='blue', bg='green')
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('Id_Kategori','Kode_Kategori','Jenis','Id_buku')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('Id_Kategori', text='ID_KATEGORI')
        self.tree.column('Id_Kategori', width="100")
        self.tree.heading('Kode_Kategori', text='KODE_KATEGORI')
        self.tree.column('Kode_Kategori', width="100")
        self.tree.heading('Jenis', text='JENIS')
        self.tree.column('Jenis', width="30")
        self.tree.heading('Id_buku', text='ID_BUKU')
        self.tree.column('Id_buku', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_Kategori.delete(0,END)
        self.txtKode_Kategori.insert(END,"")
        self.txtJenis.delete(0,END)
        self.txtJenis.insert(END,"")
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data kategori
        obj = Kategori()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["Id_Kategori"],d["Kode_Kategori"],d["Jenis"],d["Id_buku"]))
    def onCari(self, event=None):
        Kode_Kategori = self.txtKode_Kategori.get()
        obj = Kategori()
        a = obj.get_by_Kode_Kategori(Kode_Kategori)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        Kode_Kategori = self.txtKode_Kategori.get()
        obj = Kategori()
        res = obj.get_by_Kode_Kategori(Kode_Kategori)
        self.txtKode_Kategori.delete(0,END)
        self.txtKode_Kategori.insert(END,obj.Kode_Kategori)
        self.txtJenis.delete(0,END)
        self.txtJenis.insert(END,obj.Jenis)
        self.txtId_buku.delete(0,END)
        self.txtId_buku.insert(END,obj.Id_buku)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        Kode_Kategori = self.txtKode_Kategori.get()
        Jenis = self.txtJenis.get()
        Id_buku = self.txtId_buku.get()
        # create new Object
        obj = Kategori()
        obj.Kode_Kategori = Kode_Kategori
        obj.Jenis = Jenis
        obj.Id_buku = Id_buku
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_Kode_Kategori(Kode_Kategori)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        Kode_Kategori = self.txtKode_Kategori.get()
        obj = Kategori()
        obj.Kode_Kategori = Kode_Kategori
        if(self.ditemukan==True):
            res = obj.delete_by_Kode_Kategori(Kode_Kategori)
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
    aplikasi = FrmKategori(root2, "Aplikasi Data Kategori")
    root2.mainloop()