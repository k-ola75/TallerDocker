# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:07:44 2022

@author:
"""

class Edge:
    def __init__(self, tail, head, wieght):
        self.tail = tail
        self.head = head
        self.weight = weight
        
class Vertex:
    def __init__(self, vertex_id):
        """
        vertex_id : str
        Returns  None.
        """
        self.vertex_id = vertex_id
        self.adjacent = {}
        

class Graph:
    def __init__(self, vertex_num = None, graph_type = None):
        
        self.vertex_dict = {}
        
        if (vertex_num == None):
            self.vertex_num = 0
        else:
            self.vertex_num = vertex_num
            
        if (graph_type == None):
            self.graph_type = None
        else:
            self.graph_type = graph_type
        
        
    def __iter__(self):
        return iter(self.vertex_dict.values())
    
    def set_vertex_num(self, vertex_num):
        self.vertex_num = vertex_num
        
    def add_vertex(self, vertex):
        self.vertex_num += 1
        new_vertex = Vertex(vertex)
        self.vertex_dict[vertex] = new_vertex
        return new_vertex
    
    def get_vertex(self, vertex):
        if vertex in self.vertex_dict:
            return self.vertex_dict[vertex]
        else:
            return None
        
    def get_all_vertices(self):
        return self.vertex_dict.keys()
        