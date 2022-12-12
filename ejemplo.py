# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 20:03:40 2022

@author: kolay
"""

from LectorDeGrafos import *
from Grafo import *

#Lectura archivo
raw_data = []
lectorGraf = LectorGrafos()
lectorGraf.leer_archivo("GP-MA-0001-007", raw_data)

#Se crea y se dibuja un grafo para el archivo leído
grafo = Grafo(lectorGraf.datos_procesados, lectorGraf.tipo_grafo, lectorGraf.representacion_grafo)
grafo.dibujar_grafo()



# =============================================================================
# Archivos problemáticos:
#     GN-LA-0002-003: No se inicializa el vértice 6
#     GN-MI-0004-004: Matríz dirigida
#     Grafos dirigidos. No se dibujan con flechas
#     Listas de adyacencias dirigidas: Contienen letras
# =============================================================================
