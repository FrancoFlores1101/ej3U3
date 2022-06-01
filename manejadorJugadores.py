from claseJugador import jugador
from manejadorContratos import manejadorContratos
from ManejadorEquipos import manejaequipos
class manejadorjugadores:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def crear(self,unManejador:manejadorContratos,otromanejador:manejaequipos):
        print('ingrese nombre,dni,ciudad,pais,fechanacimiento')
        nom=input()
        dni=input()
        ciudad=input()
        pais=input()
        fechanacimiento=input()
        instancia=jugador(nom,dni,ciudad,pais,fechanacimiento)
        self.__lista.append(instancia)
        print('ingrese fechas del contrato y pago, junto con nombre del club')
        fecha1=input()
        fecha2=input()
        pago=float(input())
        nombre=input()
        equipo=otromanejador.obtenerInstancia()
        unManejador.crear(fecha1,fecha2,pago,nombre,instancia,equipo)
