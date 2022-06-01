import numpy as np
from claseAsociacion import contrato
class manejadorContratos:
    __dimension=10
    __cantidad=0
    __incremento=5
    __arregloContratos=None
    def __init__(self):
        self.__dimension=10
        self.__cantidad=0
        self.__incremento=5
        self.__arregloContratos=np.empty(10,dtype=contrato)
    def agregar(self,instancia):
        if self.__cantidad== self.__dimension:
            self.__dimension+=self.__incremento
            self.__arregloContratos.resize(self.__dimension)
        self.__arregloContratos[self.__cantidad]=instancia
        self.__cantidad+=1
    def crear(self,fecha1,fecha2,pago,equipo,jugador):
        unContrato=contrato(fecha1,fecha2, pago, equipo, jugador)
        self.agregar(unContrato)
    def buscar(self,dni):
        while i<self.__dimension and dni != self.__arregloContratos[i].getDNI()
            i+=1
        if i == self.__dimension
            i=-1
        return i
    def dni(self):
        print('ingrese dni a buscar')
        n=int(input())
        indice=self.buscar(n)
        if indice!= -1
            print(self.__arregloContratos[i].getEquipo(),' ',self.__arregloContratos[i].getFechaFIN())
    def jugadoresEquipo(self):
        equipo=input('ingrese el equipo')
        for contrato in self.__arregloContratos:
            if contrato.getEquipo() == equipo and ##CONDICION FECHA##:
                print(contrato.getDNI(),contrato.getNombre)
    def importetotal(self):
        equipo=input('ingrese el equipo')
        total=0
        for contrato in self.__arregloContratos:
            if contrato.getEquipo() == equipo:
                total+=contrato.getSueldo()
        print('TOTAL:',total)
