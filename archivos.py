# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 12:01:09 2022

@author: kolay
"""

class LectorGrafos:

    def __init__(self) -> None:
        self.lista_adyacencia = []
        self.vertices = []
        self.tipoGrafo = "" #Directed (D), Non-Directed (N) or Weighted (P)
        self.representacionGrafo = "" #adjacency matrix (MA), adjacency list (LA) or incidence matrix (MI)
        self.__nombredelArchivo = ""
    
    def info_generalGrafo(self, infografo: str):
        self.tipoGrafo = infografo[1]
        self.representacionGrafo = infografo[2] + infografo[3]
    
    def SetnombreArchivo(self, nombre:str):
        self.__nombredelArchivo = nombre    
    
    def guardarrepresentacionGrafo(self, tipografo: str, fila: str):
        if self.representacionGrafo == "LA":
            lista = []
            for i in fila:
                if (i != " ") & (i != "\n") & (i != ":"):
                    lista.append(i)
            self.vertices.append(lista[0])
            self.lista_adyacencia.append(lista)

        elif self.representacionGrafo == "MA":
            lista = []
            for i in fila:
                if (i != " ") & (i != "\n"):
                    lista.append(i)
            self.lista_adyacencia.append(lista)
            #lista_adyacencia[0] es la cantidad y los vertices de la matriz

        elif self.representacionGrafo == "MI":
            lista = []
            for i in fila:
                if (i != " ") & (i != "\n") & (i != ":"):
                    lista.append(i)
            self.vertices.append(lista[0])
            self.lista_adyacencia.append(lista)
            
            
    def leerGrafo(self):
        with open("grafos/" + self.__nombredelArchivo , 'r') as fichero:
            linea = fichero.readline()
            
            while linea.find("#") != -1:
                linea = fichero.readline()
            #ignora las lineas comentadas
            
            self.info_generalGrafo(linea)
            
            #inicia la lectura del grafo
            linea = fichero.readline()
            while linea != '':
                self.guardarrepresentacionGrafo(self.representacionGrafo, linea)
                linea = fichero.readline()
        
#cantidad de vértices, aristas y tipo de grafo / PRUEBAS
lectorGraf = LectorGrafos()
lectorGraf.SetnombreArchivo("GN-MI-0004-001.txt")
lectorGraf.leerGrafo()


#MATRIZ DE ADYACENCIA+/INCIDENCIA EJEMPLO
print(len (lectorGraf.lista_adyacencia[0]))# numero de vertices
print(lectorGraf.lista_adyacencia)
# =============================================================================
# for i in range(len(lectorGraf.lista_adyacencia)):
#     print(lectorGraf.lista_adyacencia[i])
# =============================================================================

# =============================================================================
# print(lectorGraf.tipoGrafo)
# print(lectorGraf.representacionGrafo)
# =============================================================================

