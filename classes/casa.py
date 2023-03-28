class Casa():

    def __init__(self):
        self.__abierta = False

    def abrir(self):
        if not self.__abierta:
            self.__abierta = True

    def getAbierta(self):
        return self.__abierta


casa = Casa()
casa.abrir()
print(casa.getAbierta())
