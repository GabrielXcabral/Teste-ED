from PilhaEncadeada import Pilha

class Jogador:
    def __init__(self, nome, maoPilha):
        self.nome = nome
        self.maoPilha = maoPilha

    #Retorna a quantidade de cartas na mão do jogador
    def quantidadeDeCartas(self):
        return self.maoPilha.tamanho()

    #Coloca a carta na base da pilha de cada jogador
    def botarCartaEmbaixo(self, cartaGanha):
        self.maoPilha.insereNoFimDaPilha(cartaGanha)

    #Mosta a jogada dos jogadores
    def carta_do_jogador(self):
        carta = self.maoPilha.desempilha()
        print("{} colocou: {}".format(self.nome, carta))
        print("\n")
        return carta
    
    def tem_carta(self):
        return self.maoPilha.estaVazia() == False

    def __str__(self):
        return "Jogador: " + self.nome + ", Quantidade de cartas na mão: " + str(self.maoPilha.tamanho())  + ", Cartas na mão: " + self.maoPilha.__str__()