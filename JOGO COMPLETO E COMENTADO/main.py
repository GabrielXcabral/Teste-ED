from ast import While
from re import S
from tkinter import E, N
from baralho import Baralho, BaralhoException
from PilhaEncadeada import Pilha
from carta import Carta
from jogador import Jogador

# Chamado quando um jogador ganha uma rodada
def ganharCartas(jogador, carta1, carta2):
    print(f'{jogador.nome} ganhou! \n')
    jogador.botarCartaEmbaixo(carta1)
    jogador.botarCartaEmbaixo(carta2)

    #Jogador ganha a rodada de empate
    if pilhaDeEmpate.estaVazia() == False:
        print(f"{jogador.nome} GANHOU A PILHA DE EMPATE {pilhaDeEmpate}")
        print("-------------------------------------------------------------------------------------- \n")

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


    # Criando baralho e dividindo para duas pessoa. Obs: As cartas já vão embaralhadas
    d= Baralho()
    print(f'Quantidade de cartas: {len(d)} \n')
    print("Deck:")
    print(f"{d} \n")
    
    mão1,mão2=d.dividir_cartas()
    print("----------------------------------------------------------------------------------- \n")

    #Criando dois jogadores

    def perguntaNome(numeroDoJogador):
        nome=input(f"Digite o nome do player {numeroDoJogador}: ")
        if len(nome) == 0:
            raise AssertionError('Nome vazio')
        return nome

    print("NOME DOS JOGADORES: \n")

    while True:
        try:
            nome = perguntaNome(1)
            jogador1 = Jogador(nome, mão1)
            break
        except AssertionError: 
            print('O usuário digitou um nome inválido')
            continue

    while True:  
        try:
            nome2 = perguntaNome(2)
            jogador2 = Jogador(nome2, mão2)
            break
        except Exception: 
            print('O usuário digitou um nome inválido')
            continue

    print("----------------------------------------------------------------------------------- \n")

    #Mostrando os parâmetros iniciais dos jogadores
    print("SITUAÇÃO DOS JOGADORES: \n")
    print (jogador1)
    print("\n")
    print (jogador2)

    print("----------------------------------------------------------------------------------- \n")

    #Jogo continua enquanto os dois jogadores tiverem pelo menos 1 carta
    while jogador1.tem_carta() and jogador2.tem_carta() and total_rounds < 100:
        print("\n")
        input("Aperte ENTER para jogar a proxima rodada\n")
        print(f"Hora de uma nova rodada #{total_rounds + 1}!!! \n")
        print("Jogue uma carta!")
        total_rounds += 1

        #Lógica do lance da carta, fica na classe Jogador

        cartaJogador2 = jogador2.carta_do_jogador()
        cartaJogador1 = jogador1.carta_do_jogador()

        # lógica de comparação fica dentro da classe carta

        # JOGADOR2 GANHOU
        if cartaJogador2 > cartaJogador1:
            ganharCartas(jogador2, cartaJogador1, cartaJogador2)

        # JOGADOR1 GANHOU
        elif cartaJogador2 < cartaJogador1:
            ganharCartas(jogador1, cartaJogador1, cartaJogador2)
        
        #ACONTECE UM EMPATE
        elif cartaJogador2 == cartaJogador1:
            contagem_de_empates += 1
            print('EMPATE')
            print("------------------------------------------------------------------------ \n")
            pilhaDeEmpate.empilha(cartaJogador1)
            pilhaDeEmpate.empilha(cartaJogador2)

        #Mostrando a situação de cada jogador em cada rodada
        print("SITUAÇÃO ATUAL DE CADA JOGADOR:")
        print (jogador1)
        print("\n")
        print (jogador2)

        if pilhaDeEmpate.estaVazia() == False:
            #print("\n")
            print(f"\n Pilha de EMPATE = {pilhaDeEmpate}")

        print("--------------------------------------------------------------------------- \n")

    #Resumo do jogo e definindo o vencedor
    print("Game over, número de rodadas:"+str(total_rounds))
    print("EMPATEs aconteceram: " + str(contagem_de_empates) +" vezes")
    if jogador1.quantidadeDeCartas() > jogador2.quantidadeDeCartas():
        print(f"{jogador1.nome} GANHOU o jogo com {jogador1.quantidadeDeCartas()} cartas!!!")
    elif jogador2.quantidadeDeCartas() > jogador1.quantidadeDeCartas():
        print(f"{jogador2.nome} GANHOU o jogo com {jogador2.quantidadeDeCartas()} cartas!!!")
    else:
        print("O JOGO TERMINOU EMPATADO")

    while True:
        try:
            querJogarNovamente = input("Quer jogar novamente (S/N)?").upper()
            assert querJogarNovamente == "S" or querJogarNovamente == "N"
            break
        except AssertionError: 
            print('Digite uma tecla válida')
            continue

print("Até logo!")
