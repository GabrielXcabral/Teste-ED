from carta import Carta
import random

class Baralho:
    def __init__(self):
        numeracao = ["As", 2,  3, 4, 5, 6, 7, 8, 9, 10, "valete", "dama", "rei" ]
        nipe = ["Ouro","Espada", "Paus", "Copas"]
        self.listaBaralho = list()
        for idx in nipe:
            for id in numeracao:
                self.listaBaralho.append (Carta(id, idx))
        self.shuffle()
    

    def __len__(self):
        return len(self.listaBaralho)

    def shuffle(self): #Embaralha as cartas
         random.shuffle(self.listaBaralho)

    def __str__(self):
        saida = ''
        for carta in self.listaBaralho:
            saida += carta.__str__() + '\n'
        return saida
    
    def dividir_cartas(self): #dividi as cartas
        return (self.listaBaralho[:26],self.listaBaralho[26:])

    def temCarta(self):  #definindo o baralho ter ou n carta. Isso vai poder ser colocado no while, pra dizer quando ele parar
        if len(self.listaBaralho) > 0:
            return True
        else:
            return False
       
    def retirarCarta(self):
        try:
            return self.listaBaralho.pop(-1) 
        except IndexError :                  
            raise BaralhoException ('Não há cartas')

class BaralhoException(Exception): #3º classe de exeção. Quando der erros jogo aqui
    def __init__(self, msg):
        super().__init__(msg)