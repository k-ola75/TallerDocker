import tkinter as tk
from tkinter import ttk


class App:

    def __init__(self):
        self.ListAD_B = None
        self.MatrixID_B = None
        self.MatrixAD_B = None
        self.AddB = None
        self.PathE = None
        self.PathL = None
        self.NameFileE = None
        self.NameFileL = None
        self.root = tk.Tk()
        self.root.resizable(False, False)
        self.root.title("graph converter")
        self.root.iconbitmap("grabar.ico")
        self.add_fileL = ttk.LabelFrame(self.root, text="Add File:")
        self.add_fileL.grid(column=0, row=0, padx=5, pady=10)
        self.login()
        self.optionsL = ttk.LabelFrame(self.root, text="Options")
        self.optionsL.grid(column=0, row=1, padx=5, pady=10)
        self.operaciones()
        self.root.mainloop()

    def login(self):
        NameFileL = ttk.Label(self.add_fileL, text="Name file:")
        NameFileL.grid(column=0, row=0, padx=4, pady=4)
        NameFileE = ttk.Entry(self.add_fileL)
        NameFileE.grid(column=1, row=0, padx=4, pady=4)
        PathL = ttk.Label(self.add_fileL, text="Path:")
        PathL.grid(column=0, row=1, padx=4, pady=4)
        PathE = ttk.Entry(self.add_fileL )
        PathE.grid(column=1, row=1, padx=4, pady=4)
        AddB = ttk.Button(self.add_fileL, text="Add")
        AddB.grid(column=1, row=2, padx=4, pady=4)

    def operaciones(self):
        MatrixAD_B = ttk.Checkbutton(self.optionsL, text="Matriz de adyacencia", onvalue=1, offvalue=0)
        MatrixAD_B.grid(column=0, row=0, padx=4, pady=4)
        MatrixID_B = ttk.Checkbutton(self.optionsL, text="Matriz de incidence", onvalue=1, offvalue=0)
        MatrixID_B.grid(column=1, row=0, padx=4, pady=4)
        ListAD_B = ttk.Checkbutton(self.optionsL, text="Lista de adyacencia", onvalue=1, offvalue=0)
        ListAD_B.grid(column=2, row=0, padx=4, pady=4)


window = App()
