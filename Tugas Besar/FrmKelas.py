import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Kelas import *
class FrmKelas:
    
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
        Label(mainFrame, text='KODE_KELAS:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_KELAS:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='SEMESTER:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtKode_kelas = Entry(mainFrame)
        self.txtKode_kelas.grid(row=0, column=1, padx=5, pady=5)
        self.txtKode_kelas.bind("<Return>", self.onCari)
        self.txtNama_kelas = Entry(mainFrame) 
        self.txtNama_kelas.grid(row=1, column=1, padx=5, pady=5)
        self.txtSemester = Entry(mainFrame)
        self.txtSemester.grid(row=2, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id_kelas','kode_kelas','nama_kelas','semester')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id_kelas', text='ID_KELAS')
        self.tree.column('id_kelas', width="100")
        self.tree.heading('kode_kelas', text='KODE_KELAS')
        self.tree.column('kode_kelas', width="100")
        self.tree.heading('nama_kelas', text='NAMA_KELAS')
        self.tree.column('nama_kelas', width="100")
        self.tree.heading('semester', text='SEMESTER')
        self.tree.column('semester', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtKode_kelas.delete(0,END)
        self.txtKode_kelas.insert(END,"")
        self.txtNama_kelas.delete(0,END)
        self.txtNama_kelas.insert(END,"")
        self.txtSemester.delete(0,END)
        self.txtSemester.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data kelas
        obj = Kelas()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id_kelas"],d["kode_kelas"],d["nama_kelas"],d["semester"]))
    def onCari(self, event=None):
        kode_kelas = self.txtKode_kelas.get()
        obj = Kelas()
        a = obj.get_by_kode_kelas(kode_kelas)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        kode_kelas = self.txtKode_kelas.get()
        obj = Kelas()
        res = obj.get_by_kode_kelas(kode_kelas)
        self.txtNama_kelas.delete(0,END)
        self.txtNama_kelas.insert(END,obj.nama_kelas)
        self.txtSemester.delete(0,END)
        self.txtSemester.insert(END,obj.semester)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        kode_kelas = self.txtKode_kelas.get()
        nama_kelas = self.txtNama_kelas.get()
        semester = self.txtSemester.get()
        # create new Object
        obj = Kelas()
        obj.kode_kelas = kode_kelas
        obj.nama_kelas = nama_kelas
        obj.semester = semester
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_kode_kelas(kode_kelas)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        kode_kelas = self.txtKode_kelas.get()
        obj = Kelas()
        obj.kode_kelas = kode_kelas
        if(self.ditemukan==True):
            res = obj.delete_by_kode_kelas(kode_kelas)
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
    aplikasi = FrmKelas(root2, "Aplikasi Data Kelas")
    root2.mainloop()
