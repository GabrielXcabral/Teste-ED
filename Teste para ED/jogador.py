class Jogador:
    def __init__(self, nome, mao):
        self.nome = nome
        self.mao = mao

    def carta_do_jogador(self):
        carta = self.mao.remove()
        print("{} colocou: {}".format(self.nome,carta))
        print("\n")
        return carta

    def pegar_carta(self):
        cartas_de_empate = []
        if len(self.mao.x)<3:
            return self.mao.x
        else:
            for x in range(3):
                cartas_de_empate.append(self.mao.x.pop())
                return cartas_de_empate

    
    def tem_carta(self):
        return len(self.mao.x) != 0