from baralho import Baralho, BaralhoException
from PilhaEncadeada import Pilha
from carta import Carta
from jogador import Jogador

# Chamado quando um jogador ganha uma rodada
def ganharCartas(jogador, carta1, carta2):
    print(f'{jogador.nome} ganhou!\n')
    jogador.botarCartaEmbaixo(carta1)
    jogador.botarCartaEmbaixo(carta2)

    if pilhaDeEmpate.estaVazia() == False:
        print(f"{jogador.nome} GANHOU A PILHA DE EMPATE {pilhaDeEmpate}")

    while pilhaDeEmpate.estaVazia() == False:
        cartaNaPilhaDeEmpate = pilhaDeEmpate.desempilha()
        jogador.botarCartaEmbaixo(cartaNaPilhaDeEmpate)

querJogarNovamente = "S"

while querJogarNovamente == "S":
    #Contadores:
    total_rounds = 0
    contagem_de_empates = 0
    pilhaDeEmpate = Pilha()

    print("Bem-vindo à guerra, vamos entrar no nosso jogo... \n")
    # Criando baralho e dividindo em para duas pessoas embaralhadas
    d= Baralho()
    print(f'Quantidade de cartas: {len(d)}')

    mão1,mão2=d.dividir_cartas()

    #Criando dois jogadores
    jogador2 = Jogador("Computador", mão2)
    nome=input("Digite seu nome: ")
    jogador1 = Jogador(nome, mão1)

    #Jogo continua enquanto os dois jogadores tiverem pelo menos 1 carta
    while jogador1.tem_carta() and jogador2.tem_carta() and total_rounds < 100:
        input("Aperte ENTER para jogar a proxima rodada\n")
        print(f"Hora de uma nova rodada #{total_rounds + 1}!!! \n")
        print("Jogue uma carta!")
        total_rounds += 1

        cartaJogador2 = jogador2.carta_do_jogador()
        cartaJogador1 = jogador1.carta_do_jogador()

        # lógica de comparação fica dentro da classe carta

        # JOGADOR2 GANHOU
        if cartaJogador2 > cartaJogador1:
            ganharCartas(jogador2, cartaJogador1, cartaJogador2)

        # JOGADOR1 GANHOU
        elif cartaJogador2 < cartaJogador1:
            ganharCartas(jogador1, cartaJogador1, cartaJogador2)

        elif cartaJogador2 == cartaJogador1:
            contagem_de_empates += 1
            print('EMPATE')
            pilhaDeEmpate.empilha(cartaJogador1)
            pilhaDeEmpate.empilha(cartaJogador2)

        print("Aqui está a classificação atual:")
        print (jogador1)
        print (jogador2)
        if pilhaDeEmpate.estaVazia() == False:
            print(f"Pilha de EMPATE = {pilhaDeEmpate}")

    print("Game over, número de rodadas:"+str(total_rounds))
    print("EMPATEs aconteceram: " + str(contagem_de_empates) +" vezes")
    if jogador1.quantidadeDeCartas() > jogador2.quantidadeDeCartas():
        print(f"{jogador1.nome} GANHOU o jogo com {jogador1.quantidadeDeCartas()} cartas!!!")
    elif jogador2.quantidadeDeCartas() > jogador1.quantidadeDeCartas():
        print(f"{jogador2.nome} GANHOU o jogo com {jogador2.quantidadeDeCartas()} cartas!!!")
    else:
        print("O JOGO TERMINOU EMPATADO")

    querJogarNovamente = input("Quer jogar novamente (S/N)?")
