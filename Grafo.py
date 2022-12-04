# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:55:07 2022

@author:
"""
import random
import turtle

class Vertice:
    def __init__(self, id_vertice, x ,y ,etiqueta):
        self.id_vertice = id_vertice
        self.x = x
        self.y = y
        self.etiqueta = etiqueta
        
class Arista:
    def __init__(self, cola, cabeza, peso=0.0):
        self.cola = cola
        self.cabeza = cabeza
        self.peso = peso
        
class Grafo:
    def __init__(self, tipo, representacion, vertices = None, aristas = None):
        if (vertices != None):
            self.vertices = vertices
        else:
            self.vertices = {}
        
        if (vertices != None):
            self.aristas = aristas
        else:
            self.aristas = []
        
        self.tipo = tipo
        self.representacio = representacion
    
    def add_vertices(self, id_vertice):
        if id_vertice not in self.vertices:
            x = random.randrange(-250, 250, 40)
            y = random.randrange(-250, 250, 40)
            etiqueta = str(id_vertice)
            nuevo_vertice = Vertice(id_vertice, x, y, etiqueta)
            self.vertices[id_vertice] = nuevo_vertice
            print("añadido", etiqueta)
    
    def add_arista(self, cola, cabeza, peso):
            nueva_arista = Arista(cola, cabeza)
            self.aristas.append(nueva_arista)
            
            if (self.tipo == "P"):
                nueva_arista.peso = peso
    
    def dibujar_grafo(self) -> None:
        turtle.speed(10)

        for arista in self.aristas:
            x1 = float(self.vertices[arista.cola].x)
            y1 = float(self.vertices[arista.cola].y)
            x2 = float(self.vertices[arista.cabeza].x)
            y2 = float(self.vertices[arista.cabeza].y)
            turtle.penup()
            turtle.goto(x1,y1)
            turtle.pendown()
            turtle.goto(x2,y2)
            if arista.peso != 0.0:       
                x = (x1 + x2) / 2
                y = (y1 + y2) / 2
                turtle.penup()
                turtle.goto(x,y)
                turtle.write(str(arista.peso),align="center",font=("Arial",12,"normal"))
            
        for vertice in self.vertices:
            vertex = self.vertices[vertice]
            x = vertex.x
            y = vertex.y
            turtle.penup()
            turtle.goto(x,y-20)
            
            turtle.pendown()
            turtle.fillcolor("blue")
            turtle.begin_fill()
            turtle.circle(10)
            turtle.end_fill()
            turtle.penup()
            turtle.goto(x+2,y+11)
            turtle.write(vertex.etiqueta,align="center",font=("Arial",12,"bold"))

        turtle.mainloop()
        turtle.done()
            