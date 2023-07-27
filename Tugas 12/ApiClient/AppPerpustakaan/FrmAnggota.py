import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Anggota import *
class FrmAnggota:
    
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
        Label(mainFrame, text='NAMA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JENIS_KELAMIN:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='ALAMAT:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NO_TELPON:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtNIM = Entry(mainFrame) 
        self.txtNIM.grid(row=0, column=1, padx=5, pady=5)
        self.txtNIM.bind("<Return>",self.onCari)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5)
        # Combo Box
        self.txtJenis_kelamin = StringVar()
        Cbo_Jenis_kelamin = ttk.Combobox(mainFrame, width = 17, textvariable = self.txtJenis_kelamin) 
        Cbo_Jenis_kelamin.grid(row=2, column=1, padx=5, pady=5)
        # Adding Jenis_kelamin combobox drop down list
        Cbo_Jenis_kelamin['values'] = ('L','P')
        Cbo_Jenis_kelamin.current()
        # Textbox
        self.txtAlamat = Entry(mainFrame) 
        self.txtAlamat.grid(row=3, column=1, padx=5, pady=5)
        self.txtNo_telpon = Entry(mainFrame) 
        self.txtNo_telpon.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10, bg='black', fg='red')
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10, fg='gold', bg='blue')
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10, fg='yellow', bg='purple')
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('Id_anggota','NIM','Nama','Jenis_kelamin','Alamat','No_telpon')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('Id_anggota', text='ID_ANGGOTA')
        self.tree.column('Id_anggota', width="100")
        self.tree.heading('NIM', text='NIM')
        self.tree.column('NIM', width="100")
        self.tree.heading('Nama', text='NAMA')
        self.tree.column('Nama', width="100")
        self.tree.heading('Jenis_kelamin', text='JENIS_KELAMIN')
        self.tree.column('Jenis_kelamin', width="100")
        self.tree.heading('Alamat', text='ALAMAT')
        self.tree.column('Alamat', width="100")
        self.tree.heading('No_telpon', text='NO_TELPON')
        self.tree.column('No_telpon', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtNIM.delete(0,END)
        self.txtNIM.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtJenis_kelamin.set("")
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,"")
        self.txtNo_telpon.delete(0,END)
        self.txtNo_telpon.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data anggota
        obj = Anggota()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["Id_anggota"],d["NIM"],d["Nama"],d["Jenis_kelamin"],d["Alamat"],d["No_telpon"]))
    def onCari(self, event=None):
        NIM = self.txtNIM.get()
        obj = Anggota()
        a = obj.get_by_NIM(NIM)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        NIM = self.txtNIM.get()
        obj = Anggota()
        res = obj.get_by_NIM(NIM)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,obj.Nama)
        self.txtJenis_kelamin.set(obj.Jenis_kelamin)
        self.txtAlamat.delete(0,END)
        self.txtAlamat.insert(END,obj.Alamat)
        self.txtNo_telpon.delete(0,END)
        self.txtNo_telpon.insert(END,obj.No_telpon)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        NIM = self.txtNIM.get()
        Nama = self.txtNama.get()
        Jenis_kelamin = self.txtJenis_kelamin.get()
        Alamat = self.txtAlamat.get()
        No_telpon = self.txtNo_telpon.get()
        # create new Object
        obj = Anggota()
        obj.NIM = NIM
        obj.Nama = Nama
        obj.Jenis_kelamin = Jenis_kelamin
        obj.Alamat = Alamat
        obj.No_telpon = No_telpon
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
        obj = Anggota()
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
    aplikasi = FrmAnggota(root2, "Aplikasi Data Anggota")
    root2.mainloop()