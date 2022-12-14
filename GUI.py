import os
import tkinter as tk
from tkinter import ttk
from LectorDeGrafos import *
from Grafo import *


class App:

    def __init__(self):
        self.graph = None
        self.raw_data_ = None
        self.lec = None
        self.Rmatrix = None
        self.RepresentationL = None
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
        #self.root.iconbitmap("grabar.ico")
        self.add_fileL = ttk.LabelFrame(self.root, text="Add File:")
        self.add_fileL.grid(column=0, row=0, padx=5, pady=10)
        self.add_file()
        self.root.mainloop()

    def add_file(self):
        self.NameFileL = ttk.Label(self.add_fileL, text="Name file:")
        self.NameFileL.grid(column=0, row=0, padx=4, pady=4)
        self.NameFileE = ttk.Entry(self.add_fileL)
        self.NameFileE.grid(column=1, row=0, padx=4, pady=4)
        AddB = ttk.Button(self.add_fileL, text="Add", command=self.send_date)
        AddB.grid(column=1, row=2, padx=4, pady=4)


    def options(self,window):
        MatrixAD_B = ttk.Button(window, text="adjacency matrix", command=self.change_MAD)
        MatrixAD_B.grid(column=0, row=0, padx=4, pady=4)
        MatrixID_B = ttk.Button(window, text="Matriz de incidence", command=self.change_MAI)
        MatrixID_B.grid(column=1, row=0, padx=4, pady=4)
        ListAD_B = ttk.Button(window, text="incidence list", command=self.change_LSI)
        ListAD_B.grid(column=2, row=0, padx=4, pady=4)

    def search(self, path):
        if path is not None:
            print(os.getcwd())
            self.homeP = os.getcwd()
            os.chdir(path)
            print(os.getcwd())



    def sub_page(self, VT, TG, RG, ED):
        self.sub_page_matrix = tk.Tk()
        self.sub_page_matrix.title("Graph Representation")
        #self.sub_page_matrix.iconbitmap("grabar.ico")
        self.InformationL = ttk.Labelframe(self.sub_page_matrix, text="Graph Information")
        self.InformationL.grid(column=0, row=0, pady=10)
        self.information(VT,TG,RG,ED)
        self.changeRL = ttk.Labelframe(self.sub_page_matrix, text="change type representation")
        self.changeRL.grid(column=0, row=1, padx=5, pady=10)
        self.options(self.changeRL)
        #self.sub_page_matrix.mainloop()

    def information(self, VT, TG, RG, ED):
        self.VerticesL = ttk.Label(self.InformationL, text="Vertices: ")
        self.VerticesL.grid(column=0, row=0, padx=3, pady=5)
        self.verticesI = ttk.Label(self.InformationL,text=VT)
        self.verticesI.grid(column=1, row=0, padx=3, pady=5)
        self.aristasL = ttk.Label(self.InformationL, text="edges: ")
        self.aristasL.grid(column=0, row=1, padx=3, pady=5)
        self.aristasI = ttk.Label(self.InformationL, text=ED)
        self.aristasI.grid(column=1,row=1,padx=3,pady=5 )
        self.typegrafoL = ttk.Label(self.InformationL, text="type graph: ")
        self.typegrafoL.grid(column=0, row=2, padx=3, pady=5)
        self.typegrafoUI = ttk.Label(self.InformationL, text=TG)
        self.typegrafoUI.grid(column=1, row=2, padx=3, pady=5)
        self.repregrafoL = ttk.Label(self.InformationL, text="representation: ")
        self.repregrafoL.grid(column=0, row=3, padx=3, pady=5)
        self.repregrafoI= ttk.Label(self.InformationL,text=RG)
        self.repregrafoI.grid(column=1, row=3, padx=3, pady=5)


    def send_date(self):
        self.lec = LectorGrafos()
        self.raw_data_ = []
        self.lec.leer_archivo(self.NameFileE.get(),self.raw_data_)
        self.graph = Grafo(self.lec.datos_procesados,self.lec.tipo_grafo,self.lec.representacion_grafo)
        self.graph.dibujar_grafo()
        print(self.lec.datos)
        print(self.graph)
        print(self.graph.get_aristas())
        print(self.graph.get_tipo())
        print(self.graph.get_representacion())
        print(self.graph.to_lista_adyacencia())
        print(self.graph.to_matriz_incidencia())
        self.sub_page(self.graph.get_vertices_id(), self.graph.get_tipo(), self.graph.get_representacion(), self.graph.get_aristas())
        #self.NameFileE.delete(0, 'end')

    def change_MAD(self):
        self.MAD = tk.Toplevel()
        self.Rmatrix = ttk.Labelframe(self.MAD, text="Adjacency matrix: ")
        self.Rmatrix.grid(column=0, row=0, padx=3, pady=5)
        self.repregrafoL = ttk.Label(self.Rmatrix, text=self.graph.to_matriz_adyacencia())
        self.repregrafoL.grid(column=1, row=0, padx=3, pady=5)

    def change_MAI(self):
        self.MAD = tk.Toplevel()
        self.Rmatrix = ttk.Labelframe(self.MAD, text="Incidence matrix: ")
        self.Rmatrix.grid(column=0, row=0, padx=3, pady=5)
        self.repregrafoL = ttk.Label(self.Rmatrix, text=self.graph.to_matriz_incidencia())
        self.repregrafoL.grid(column=0, row=1, padx=3, pady=5)

    def change_LSI(self):
        self.MAD = tk.Toplevel()
        self.Rmatrix = ttk.Labelframe(self.MAD, text="incidence list: ")
        self.Rmatrix.grid(column=0, row=0, padx=3, pady=5)
        self.repregrafoL = ttk.Label(self.Rmatrix, text=self.graph.to_lista_adyacencia())
        self.repregrafoL.grid(column=0, row=1, padx=3, pady=5)





