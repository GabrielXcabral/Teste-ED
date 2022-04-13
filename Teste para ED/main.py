from baralho import Baralho, BaralhoException
from carta import Carta
from jogador import Jogador


print("Bem-vindo à guerra, vamos entrar no nosso jogo... \n")
# Criando baralho e dividindo em para duas pessoas embaralhadas
d= Baralho()
print(f'Quantidade de cartas: {len(d)}')
#print(d)

mão1,mão2=d.dividir_cartas()
#print (mão1.tamanho())
#print (mão2.tamanho())


#Criando dois jogadores
jogador2 = Jogador("Computador", mão2)
nome=input("Digite seu nome: ")
jogador1 = Jogador(nome, mão1)

#Contadores:
total_rounds = 0
contagem_de_empates = 0

#fazendo o jogo andar (TESTE):
for i in range (26):
    input("Aperte ENTER para continuar o jogo")
    total_rounds += 1  
    print("Aqui está a classificação atual:")
    print (jogador1)
    print (jogador2)

    print('\n')
    print("Hora de uma nova rodada!!! \n")
    print("Jogue uma carta!")

    pilhaDeEmpate = Pilha()

    cartaJogador2 = jogador2.carta_do_jogador()
    cartaJogador1 = jogador1.carta_do_jogador()

    # carta > carta
    if cartaJogador2 > cartaJogador1:
        print(f'{jogador2.nome} ganhou!')
        jogador2.colocaCartaNoCemiterio(cartaJogador2)
        jogador2.colocaCartaNoCemiterio(cartaJogador1)
    elif cartaJogador2 < cartaJogador1:
        print(f'{jogador1.nome} ganhou!')
        jogador1.colocaCartaNoCemiterio(cartaJogador2)
        jogador1.colocaCartaNoCemiterio(cartaJogador1)
    elif cartaJogador2 == cartaJogador1:
        contagem_de_empates += 1
        print('EMPATE')

print("Game over,número de rodadas:"+str(total_rounds))
print("Uma guerra aconteceu: " + str(contagem_de_empates) +" vezes")
print("O computador ainda tem cartas?\t",str(jogador2.tem_carta()))
print("O jogador Humano ainda tem cartas?\t:",str(jogador1.tem_carta()))