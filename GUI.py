import os
import tkinter as tk
from tkinter import ttk
from LectorDeGrafos import *


class App:

    def __init__(self):
        self.typeGrafoL = None
        self.aristasL = None
        self.changeRL = None
        self.VerticesL = None
        self.InformationL = None
        self.homeP = None
        self.sub_page_matrix = None
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
        self.add_file()
        self.optionsL = ttk.LabelFrame(self.root, text="Options")
        self.optionsL.grid(column=0, row=1, padx=5, pady=10)
        self.options(self.optionsL)
        self.root.mainloop()

    def add_file(self):
        self.NameFileL = ttk.Label(self.add_fileL, text="Name file:")
        self.NameFileL.grid(column=0, row=0, padx=4, pady=4)
        self.NameFileE = ttk.Entry(self.add_fileL)
        self.NameFileE.grid(column=1, row=0, padx=4, pady=4)
        self.PathL = ttk.Label(self.add_fileL, text="Path:")
        self.PathL.grid(column=0, row=1, padx=4, pady=4)
        self.PathE = ttk.Entry(self.add_fileL)
        self.PathE.grid(column=1, row=1, padx=4, pady=4)
        AddB = ttk.Button(self.add_fileL, text="Add", command=self.send_date)
        AddB.grid(column=1, row=2, padx=4, pady=4)

    def options(self,window):
        MatrixAD_B = ttk.Checkbutton(window, text="Matriz de adyacencia", onvalue=1, offvalue=0)
        MatrixAD_B.grid(column=0, row=0, padx=4, pady=4)
        MatrixID_B = ttk.Checkbutton(window, text="Matriz de incidence", onvalue=1, offvalue=0)
        MatrixID_B.grid(column=1, row=0, padx=4, pady=4)
        ListAD_B = ttk.Checkbutton(window, text="Lista de adyacencia", onvalue=1, offvalue=0)
        ListAD_B.grid(column=2, row=0, padx=4, pady=4)

    def search(self, path):
        if path is not None:
            print(os.getcwd())
            self.homeP = os.getcwd()
            os.chdir(path)
            print(os.getcwd())



    def sub_page(self):
        self.sub_page_matrix = tk.Tk()
        self.sub_page_matrix.title("Graph Representation")
        self.sub_page_matrix.iconbitmap("grabar.ico")
        self.InformationL = ttk.Labelframe(self.sub_page_matrix, text="Grafo Information")
        self.InformationL.grid(column=0, row=0, pady=10)
        self.information()
        self.changeRL = ttk.Labelframe(self.sub_page_matrix, text="change type representation")
        self.changeRL.grid(column=0, row=1, padx=5, pady=10)
        self.options(self.changeRL)
        self.sub_page_matrix.mainloop()

    def information(self):
        self.VerticesL = ttk.Label(self.InformationL, text="Vertices: ")
        self.VerticesL.grid(column=0, row=0, padx=5, pady=5)
        self.aristasL = ttk.Label(self.InformationL, text="edges: ")
        self.aristasL.grid(column=0, row=1, padx=5, pady=5)
        self.typeGrafoL = ttk.Label(self.InformationL,text="type grafo")
        self.typeGrafoL.grid(column=0,row=2,padx=5, pady=5)


    def send_date(self):
        self.search(self.PathE.get())
        lec = LectorGrafos()
        lec.SetnombreArchivo(self.NameFileE.get())
        lec.set_path(self.PathE.get())
        lec.leerGrafo()
        print(lec.lista_adyacencia)
        os.chdir(self.homeP)
        self.sub_page()





