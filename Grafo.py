# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 19:31:22 2022

@author: kolay
"""
import sys
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
    def __init__(self, data, tipo, representacion, vertices = None, aristas = None):
        if (vertices != None):
            self.vertices = vertices
        else:
            self.vertices = {}
        
        if (aristas != None):
            self.aristas = aristas
        else:
            self.aristas = []

        self.data = data
        self.tipo = tipo
        self.representacion = representacion
        self.set_vertices()
        self.set_aristas()
    
    def add_vertice(self, id_vertice):
        if id_vertice not in self.vertices:
            x = random.randrange(-250, 250, 40)
            y = random.randrange(-250, 250, 40)
            etiqueta = str(id_vertice)
            nuevo_vertice = Vertice(id_vertice, x, y, etiqueta)
            self.vertices[id_vertice] = nuevo_vertice
            print("añadido vertice", etiqueta)
    
    def add_arista(self, cola, cabeza, peso = None):
            nueva_arista = Arista(cola, cabeza)
            self.aristas.append(nueva_arista)
            print("añadido aristta", cola, cabeza)
            if (self.tipo == "P"):
                nueva_arista.peso = peso

    def set_vertices(self):
      if (self.representacion == "MA" or self.representacion == "MI"):
        for vertice in range(self.data.shape[0]):
          self.add_vertice(vertice)
          
      elif (self.representacion == "LA"):
        for vertice in self.data:
          self.add_vertice(vertice)


    def set_aristas(self):
      if(self.representacion == "MA"):
        for cola in range(self.data.shape[0]):
          for cabeza in range(self.data.shape[1]):
              if self.data[cola,cabeza] != 0.0:
                  #print(cola, cabeza)
                  peso = self.data[cola,cabeza]
                  self.add_arista(cola, cabeza, peso)
      
      elif (self.representacion == "LA"):
        for cola in self.data:
          for cabeza in self.data[cola]:
            print(cola, cabeza)
            peso = 0.0
            self.add_arista(cola, cabeza, peso)
      
      elif (self.representacion == "MI"):
        for arista in range(self.data.shape[1]):
          cola = None
          cabeza = None
          peso = 0.0
          for vertice in range(self.data.shape[0]):
            if (self.data[vertice, arista] == 0.0):
              continue
            else:
              if (cola == None): 
                cola = vertice
                print(cola)
              else:
                cabeza = vertice
                print(cabeza)
              if (cola != None and cabeza != None):
                self.add_arista(cola, cabeza, peso)
              
    def dibujar_grafo(self):
        turtle.speed(10)
        for vertice in self.vertices:
            vertex = self.vertices[vertice]
            x = vertex.x
            y = vertex.y
            print(vertex, "x: ", x,"y: ", y)
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
            
        for arista in self.aristas:
            if(arista.cola != arista.cabeza):
                x1 = float(self.vertices[arista.cola].x)
                y1 = float(self.vertices[arista.cola].y)
                x2 = float(self.vertices[arista.cabeza].x)
                y2 = float(self.vertices[arista.cabeza].y)
                print(x1, y1, x2, y2)
                
                turtle.penup()
                turtle.goto(x1,y1)
                turtle.pendown()
                turtle.goto(x2,y2)
            else:
                x1 = float(self.vertices[arista.cola].x) 
                y1 = float(self.vertices[arista.cola].y)
                print(x1, y1)
                turtle.penup()
                turtle.goto(x1,y1 - 20)
                turtle.pendown()
                turtle.circle(15, 340)
                
            if self. tipo == "P" and arista.peso != 0.0:       
                x = (x1 + x2) / 2
                y = (y1 + y2) / 2
                turtle.penup()
                turtle.goto(x,y)
                turtle.write(str(arista.peso),align="center",font=("Arial",12,"normal"))
        turtle.mainloop()
        turtle.done()
        sys.exit(1)