# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 19:36:26 2022

@author: kolay
"""
from archivos import *
from Grafo import *
import numpy as np


#Lectura archivo
lectorGraf = LectorGrafos()
lectorGraf.SetnombreArchivo("GN-MA-0001-004.txt")
lectorGraf.leerGrafo()

#arreglo numpy facilita lectura columnas y filas de la matriz. Puede no ser necesario
matriz_datos = np.array(lectorGraf.lista_adyacencia)


#Se crea un grafo para el archivo leído
grafo = Grafo(lectorGraf.tipoGrafo, lectorGraf.representacionGrafo)


#Se añaden vertices al grafo para el archivo leído
for vertice in range(matriz_datos.shape[0]):
    grafo.add_vertices(vertice)

#se añaden aristas al grafo para el archivo leído
for cola in range(matriz_datos.shape[0]):
    for cabeza in range(matriz_datos.shape[1]):
        peso = matriz_datos[cola][cabeza]
        if peso != 0.0:
            grafo.add_arista(cola, cabeza, peso)
            

grafo.dibujar_grafo()