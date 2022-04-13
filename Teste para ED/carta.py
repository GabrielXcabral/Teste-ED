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

    # Eh Menor que
    def __lt__(self, outraCarta):
        valorDaMinhaCarta = self.converteCartaParaValorNumerico(self.__numeracao)
        valorDaOutraCarta = self.converteCartaParaValorNumerico(outraCarta.__numeracao)
        return valorDaMinhaCarta < valorDaOutraCarta

    # Eh Maior que
    def __gt__(self, outraCarta):
        valorDaMinhaCarta = self.converteCartaParaValorNumerico(self.__numeracao)
        valorDaOutraCarta = self.converteCartaParaValorNumerico(outraCarta.__numeracao)
        return valorDaMinhaCarta > valorDaOutraCarta

    # Eh igual
    def __eq__(self, outraCarta):
        valorDaMinhaCarta = self.converteCartaParaValorNumerico(self.__numeracao)
        valorDaOutraCarta = self.converteCartaParaValorNumerico(outraCarta.__numeracao)
        return valorDaMinhaCarta == valorDaOutraCarta

    def converteCartaParaValorNumerico(self, valorDaCarta):
        if isinstance(valorDaCarta, int) == False:
            if valorDaCarta == "As":
                valorDaCarta = 1
            elif valorDaCarta == "valete": 
                valorDaCarta = 11
            elif valorDaCarta == "dama": 
                valorDaCarta = 12
            elif valorDaCarta == "rei": 
                valorDaCarta = 13
        return valorDaCarta
