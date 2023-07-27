import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Dokter import *
class FrmDokter:
    
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
        Label(mainFrame, text='NIP:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JENISKELAMIN:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='SPESIALIS:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNip = Entry(mainFrame) 
        self.txtNip.grid(row=0, column=1, padx=5, pady=5)
        self.txtNip.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJenisKelamin = StringVar()
        Cbo_JenisKelamin = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJenisKelamin) 
        Cbo_JenisKelamin.grid(row=2, column=1, padx=5, pady=5)
        # Adding JenisKelamin combobox drop down list
        Cbo_JenisKelamin['values'] = ('L','P')
        Cbo_JenisKelamin.current()
        # Textbox
        self.txtSpesialis = Entry(mainFrame) 
        self.txtSpesialis.grid(row=3, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('iddokter','Nip','Nama','JenisKelamin','Spesialis')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('iddokter', text='IDDOKTER')
        self.tree.column('iddokter', width="100")
        self.tree.heading('Nip', text='NIP')
        self.tree.column('Nip', width="100")
        self.tree.heading('Nama', text='NAMA')
        self.tree.column('Nama', width="100")
        self.tree.heading('JenisKelamin', text='JENISKELAMIN')
        self.tree.column('JenisKelamin', width="100")
        self.tree.heading('Spesialis', text='SPESIALIS')
        self.tree.column('Spesialis', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNip.delete(0,END)
        self.txtNip.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJenisKelamin.set("")
        self.txtSpesialis.delete(0,END)
        self.txtSpesialis.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data dokter
        obj = Dokter()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["iddokter"],d["Nip"],d["Nama"],d["JenisKelamin"],d["Spesialis"]))
    def onCari(self, event=None):
        Nip = self.txtNip.get()
        obj = Dokter()
        a = obj.get_by_Nip(Nip)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        Nip = self.txtNip.get()
        obj = Dokter()
        res = obj.get_by_Nip(Nip)
        self.txtNip.delete(0,END)
        self.txtNip.insert(END,obj.Nip)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.Nama)
        self.txtJenisKelamin.set(obj.JenisKelamin)
        self.txtSpesialis.delete(0,END)
        self.txtSpesialis.insert(END,obj.Spesialis)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        Nip = self.txtNip.get()
        Nama = self.txtNama.get()
        JenisKelamin = self.txtJenisKelamin.get()
        Spesialis = self.txtSpesialis.get()
        # create new Object
        obj = Dokter()
        obj.Nip = Nip
        obj.Nama = Nama
        obj.JenisKelamin = JenisKelamin
        obj.Spesialis = Spesialis
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_Nip(Nip)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        Nip = self.txtNip.get()
        obj = Dokter()
        obj.Nip = Nip
        if(self.ditemukan==True):
            res = obj.delete_by_Nip(Nip)
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
    aplikasi = FrmDokter(root2, "Aplikasi Data Dokter")
    root2.mainloop()