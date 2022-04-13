class Carta:
    def __init__ (self, numeracao, nipe):
        self.__numeracao = numeracao #Estamos deixando elas privadas
        self.__nipe = nipe
    
    @property
    def nipe (self):
        return self.__nipe

    @property
    def numeracao (self):
        return self.__numeracao
    
    def __str__(self):
        return f'{self.__numeracao} de {self.__nipe}'