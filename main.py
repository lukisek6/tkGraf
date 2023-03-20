#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
import pylab as pl
import os.path

# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)


class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "BEN"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="tkGraf")
        self.lbl.pack()

        self.fileFrame = tk.LabelFrame(self, text="Soubor")
        self.fileFrame.pack(padx=5,pady=5,fill="x")
        self.fileEntry = MyEntry(self.fileFrame)
        self.fileEntry.pack(fill="x")
        self.fileBtn = tk.Button(self.fileFrame,text="...",command=self.selectFile)
        self.fileBtn.pack(anchor="e")
        
        self.dataformatVar = tk.StringVar(value="ROW")
        self.rowRadio = tk.Radiobutton(self.fileFrame, text="Data v řádcích",variable=self.dataformatVar,value="ROW")
        self.rowRadio.pack(anchor="w")
        self.columRadio = tk.Radiobutton(self.fileFrame, text="Data ve sloupcích",variable=self.dataformatVar,value="COLUM")
        self.columRadio.pack(anchor="w")

        self.grafFrame = tk.LabelFrame(self, text="Graf")
        self.grafFrame.pack(fill="x")

        tk.Label(self.grafFrame,text="Title").grid(row=0,column=0)
        self.titleEdit = MyEntry(self.grafFrame)
        self.titleEdit.grid(row=0,column=1)

        tk.Label(self.grafFrame,text="Osa X").grid(row=1,column=0)
        self.xEdit = MyEntry(self.grafFrame)
        self.xEdit.grid(row=1,column=1)

        tk.Label(self.grafFrame,text="Osa Y").grid(row=2,column=0)
        self.yEdit = MyEntry(self.grafFrame)
        self.yEdit.grid(row=2,column=1)

        tk.Label(self.grafFrame,text="Mřížka").grid(row=3,column=0)
        self.gridVar = tk.BooleanVar(value=True)
        self.gridcheck = tk.Checkbutton(self.grafFrame,variable=self.gridVar)
        self.gridcheck.grid(row=3,column=1)

        tk.Label(self.grafFrame,text="čára").grid(row=4,column=0)
        self.lineCBox = ttk.Combobox(self.grafFrame,values=("none","-","--","-.",":"))
        self.lineCBox.grid(row=4,column=1)

        self.markerVar = tk.StringVar(value="none")
        tk.Label(self.grafFrame,text="marker").grid(row=5,column=0)
        tk.OptionMenu(self.grafFrame,self.lineCBox,"none","+","x","1","o").grid(row=5,column=1,sticky="w")

        tk.Button(self, text="vykreslit",command=self.plot).pack(anchor="w")

        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack(anchor="e")

    def selectFile(self):
        self.fileEntry.value=tk.filedialog.askopenfilename()

    def plot(self):
        if not os.path.isfile(self.fileEntry.value):
            return
        with open(self.fileEntry.value,"r") as f:
            if self.dataformatVar.get() == "ROW":
                x = f.readline().split(";")
                y = f.readline().split(";")
                x = [float(i.replace(",",".")) for i in x]
                y = [float(i.replace(",",".")) for i in y]
            elif self.dataformatVar.get() == "COLUM":
                x =[]
                y =[]
                while True:
                    line = f.readline()
                    if line == "":
                        break
                    else:
                        if ";" not in line:
                            continue
                        x1,y1 = line.split(";")
                        x.append(float(x1.replace(",",".")))
                        y.append(float(y1.replace(",",".")))
        pl.plot(x,y,linestyle=self.lineCBox.get())
        pl.title(self.titleEdit.value)
        pl.xlabel(self.xEdit.value)
        pl.ylabel(self.yEdit.value)
        pl.grid(self.gridVar.get())
        pl.show()

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()