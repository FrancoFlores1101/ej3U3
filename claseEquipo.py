class equipo:
    __nombre=None
    __ciudad=None
    def __init__(self,nombre,ciudad):
        self.__nombre=nombre
        self.__ciudad=ciudad
    def getNombre(self):
        return self.__nombre
