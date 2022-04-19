from carta import Carta
from PilhaEncadeada import Pilha
import random

class Baralho:
    def __init__(self):
        numeracao = ["As", 2,  3, 4, 5, 6, 7, 8, 9, 10, "valete", "dama", "rei" ]
        nipe = ["Ouro","Espada", "Paus", "Copas"]
        self.pilhaBaralho = Pilha()
        listaCartas = list()

        for idx in nipe:
            for id in numeracao:
                listaCartas.append(Carta(id, idx))
        random.shuffle(listaCartas)

        for carta in listaCartas:
            self.pilhaBaralho.empilha(carta)


    def __len__(self):
        return self.pilhaBaralho.tamanho()

    def __str__(self):
        return self.pilhaBaralho.__str__()
    
    def dividir_cartas(self): #dividi as cartas
        primeiraMetade = Pilha()
        segundaMetade = Pilha()
        while self.pilhaBaralho.estaVazia() == False:
            cartaTirada = self.pilhaBaralho.desempilha()
            if self.pilhaBaralho.tamanho() >= 26:
                segundaMetade.empilha(cartaTirada)
            else:
                primeiraMetade.empilha(cartaTirada)
        return (primeiraMetade, segundaMetade)  

    def temCarta(self):
        if self.pilhaBaralho.tamanho() > 0:
            return True
        else:
            return False
       
    def retirarCarta(self):
        try:
            return self.pilhaBaralho.desempilha()
        except IndexError :                  
            raise BaralhoException ('Não há cartas')

class BaralhoException(Exception): #3º classe de exeção. Quando der erros jogo aqui
    def __init__(self, msg):
        super().__init__(msg)