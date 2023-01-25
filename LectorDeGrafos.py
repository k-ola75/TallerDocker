import numpy as np
import _mssql 

class LectorGrafos:
    
    def __init__(self) -> None:
        self.datos = None
        self.datos_procesados = None
        self.tipo_grafo = "" #Directed (D), Non-Directed (N) or Weighted (P)
        self.representacion_grafo = "" #adjacency matrix (MA), adjacency list (LA) or incidence matrix (MI)        
    
    def leer_archivo(self, nombre_archivo:str, raw_data:list):
        """
        Lee archivo que almacene información de un grafo (JAPeTo) e inicializa características de dicho grafo
        nombre_archivo : str
        raw_data : list, lista que almacenará datos leídos
        Returns: None.
        """
        
        #agregar aqui las credenciales de la base de datos cuando esta este creada
        server = 'localhost'
        user = 'root'
        password = 'admin123'
        database = 'grafos'
        conectDatabase = _mssql.connect(server, user, password, database)
        
        conectDatabase.execute_query('SELECT contenidoGrafo FROM grafos WHERE tituloGrafo= ' + nombre_archivo)
        
        for line in conectDatabase:
            if not line.startswith('#'):
                raw_data.append(line.split())
        
        self.datos = raw_data
        self.set_tipo_grafo(self.datos)
        self.set_representation_grafo(self.datos)
        self.set_datos_grafo(self.datos)
        
        conectDatabase.close()
                    
    def set_tipo_grafo(self, raw_data:list):
        """
        raw_data : list, lista que almacena datos sin precesar de un grafo
        Returns: None.
        """
        self.tipo_grafo = str(raw_data[0][0][1])
        
    def set_representation_grafo(self, raw_data:list):
        """
        raw_data : list, lista que almacena datos sin precesar de un grafo
        Returns: None.
        """
        self.representacion_grafo = str(raw_data[0][0][2:])
     
    def set_datos_grafo(self, raw_data):
        """
        raw_data : list, lista que almacena datos sin precesar de un grafo
        Returns: None.
        """
        if (self.representacion_grafo == "MA" or self.representacion_grafo == "MI" ):
             np_arr = np.array(raw_data[1:], dtype=(float))
             self.datos_procesados = np_arr
         
        elif (self.representacion_grafo == "LA"):
             self.datos_procesados = {}
             try:
                 vertice = 0
                 for adyacentes in raw_data[1:]:
                     adyacentes_int = [eval(i) for i in adyacentes]
                     self.datos_procesados[vertice] = adyacentes_int
                     vertice += 1
             except NameError:
                  vertice = 65
                  for adyacentes in raw_data[1:]:
                    temp = []
                    for vertex in adyacentes:
                      temp.append(ord(vertex))
                    self.datos_procesados[vertice] = temp
                    vertice += 1       
                  print("Lista de adyacencia con letras")
