import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Dosen import *
class FrmDosen:
    
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
        Label(mainFrame, text='NIDN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JK:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='PRODI:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JABATAN:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNidn = Entry(mainFrame) 
        self.txtNidn.grid(row=0, column=1, padx=5, pady=5)
        self.txtNidn.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJk = StringVar()
        Cbo_jk = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJk) 
        Cbo_jk.grid(row=2, column=1, padx=5, pady=5)
        # Adding jk combobox drop down list
        Cbo_jk['values'] = ('L','P')
        Cbo_jk.current()
        # Textbox
        self.txtProdi = Entry(mainFrame) 
        self.txtProdi.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtJabatan = Entry(mainFrame) 
        self.txtJabatan.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('nid','nidn','nama','jk','prodi','jabatan')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('nid', text='NID')
        self.tree.column('nid', width="100")
        self.tree.heading('nidn', text='NIDN')
        self.tree.column('nidn', width="100")
        self.tree.heading('nama', text='NAMA')
        self.tree.column('nama', width="100")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="100")
        self.tree.heading('prodi', text='PRODI')
        self.tree.column('prodi', width="100")
        self.tree.heading('jabatan', text='JABATAN')
        self.tree.column('jabatan', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNidn.delete(0,END)
        self.txtNidn.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJk.set("")
        self.txtProdi.delete(0,END)
        self.txtProdi.insert(END,"")
        self.txtJabatan.delete(0,END)
        self.txtJabatan.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data dosen
        obj = Dosen()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["nid"],d["nidn"],d["nama"],d["jk"],d["prodi"],d["jabatan"]))
    def onCari(self, event=None):
        nidn = self.txtNidn.get()
        obj = Dosen()
        a = obj.get_by_nidn(nidn)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        nidn = self.txtNidn.get()
        obj = Dosen()
        res = obj.get_by_nidn(nidn)
        self.txtNidn.delete(0,END)
        self.txtNidn.insert(END,obj.nidn)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.nama)
        self.txtJk.set(obj.jk)
        self.txtProdi.delete(0,END)
        self.txtProdi.insert(END,obj.prodi)
        self.txtJabatan.delete(0,END)
        self.txtJabatan.insert(END,obj.jabatan)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        nidn = self.txtNidn.get()
        nama = self.txtNama.get()
        jk = self.txtJk.get()
        prodi = self.txtProdi.get()
        jabatan = self.txtJabatan.get()
        # create new Object
        obj = Dosen()
        obj.nidn = nidn
        obj.nama = nama
        obj.jk = jk
        obj.prodi = prodi
        obj.jabatan = jabatan
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_nidn(nidn)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        nidn = self.txtNidn.get()
        obj = Dosen()
        obj.nidn = nidn
        if(self.ditemukan==True):
            res = obj.delete_by_nidn(nidn)
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
    aplikasi = FrmDosen(root2, "Aplikasi Data Dosen")
    root2.mainloop()