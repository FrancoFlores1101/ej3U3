from claseEquipo import equipo
from claseJugador import jugador

class contrato:
    __fecha1=None
    __fecha2=None
    __pago=None
    __equipo=None
    __jugador=None
    def __init__(self,fecha1,fecha2,pago,unequipo:equipo,unjugador:jugador):
        self.__fecha1=fecha1
        self.__fecha2=fecha2
        self.__pago=pago
        self.__equipo=unequipo
        self.__jugador=unjugador
    def getDNI(self):
        return self.__jugador.getdni()
    def getEquipo(self):
        return self.__equipo.getNombre()
    def getFechaFIN(self):
        return self.__fecha2
    def getNombre(self):
        return self.__jugador.getnombre()
    def getSueldo(self):
        return self.__pago
