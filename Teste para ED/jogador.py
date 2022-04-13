from PilhaEncadeada import Pilha

class Jogador:
    def __init__(self, nome, maoPilha):
        self.nome = nome
        self.maoPilha = maoPilha
        self.cemiterio = Pilha()


    def colocaCartaNoCemiterio(self, cartaGanha):
        self.cemiterio.empilha(cartaGanha)

    def carta_do_jogador(self):
        carta = self.maoPilha.desempilha()
        print("{} colocou: {}".format(self.nome, carta))
        print("\n")
        return carta

    def pegar_carta(self):
        pass
    
    def tem_carta(self):
        return self.maoPilha.estaVazia() == False

    def __str__(self):
        return "Jogador: " + self.nome + ", Cartas na mão: " + str(self.maoPilha.tamanho()) +  ", Cartas no cemiterio: " + str(self.cemiterio.tamanho()) + ", Cartas na mão: " + self.maoPilha.__str__()