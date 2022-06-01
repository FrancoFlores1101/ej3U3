class jugador:
    __nombre=None
    __DNI=None
    __ciudad=None
    __pais=None
    __fecha=None
    def __init__(self,nom,dni,ciu,pais,fecha):
        self.__nombre=nom
        self.__DNI=dni
        self.__ciudad=ciu
        self.__pais=pais
        self.__fecha=fecha
    def getdni(self):
        return self.__DNI
    def getnombre(self):
        return self.__nombre
