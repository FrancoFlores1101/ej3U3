import csv
import numpy as np
from claseEquipo import  equipo
class manejaequipos:
    __dimension=10
    __cantidad=0
    __incremento=5
    __arreglo=None
    def __init__(self):
        self.__dimension=10
        self.__cantidad=0
        self.__incremento=5
        self.__arreglo=np.empty(10,dtype=equipo)
    def agregar(self,instancia):
        if self.__cantidad== self.__dimension:
            self.__dimension+=self.__incremento
            self.__arreglo=np.resize(self.__dimension)
        self.__arreglo[self.__cantidad]=instancia
        self.__cantidad+=1
    def leercsv(self):
        archivo=open('equipos.csv')
        reader=csv.reader(archivo,delimiter=';')
        for row in reader:
            instancia=equipo(row[0],row[1])
            self.agregar(instancia)
    def buscar(self,nombre):
        i=0
        while i < self.__dimension and nombre != self.__arreglo[i].getNombre():
            i+=1
        if i == self.__dimension:
            i=-1
        return i
    def obtenerInstancia(self,nombre):
        indice=self.buscar(nombre)
        if indice != -1
            instancia=self.__arreglo[i]
        return instancia



