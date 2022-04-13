from baralho import Baralho, BaralhoException
from carta import Carta
from jogador import Jogador
from mão import Mão

#ba1 = Baralho()
#print(f'Quantidade de cartas: {len(ba1)}') #chamando o def __len__(self): lá de Baralho

#print(f'\nCartas do baralho:')
#print(ba1)

#print(f'\nCarta retirada')
#print(ba1.retirarCarta()) #uma forma diferente de fazer a mesma coisa que fizemos aqui a baixo.
#print(f'Quantidade de cartas atualmente: {len(ba1)}')

#print(f'\nCarta retirada')
#c = ba1.retirarCarta()
#print(f'Carta: {c}')
#print(f'Quantidade de cartas atualmente {len(ba1)}')

#Vamos fazer o programa fazer a retirada das cartas automaticamente:
#print(f'\nRetiranto cartas:')
#while(True):
#    try:
#        c = ba1.retirarCarta()
#        print(f'Carta: {c}. Quantidade de Cartas: {len(ba1)}' + '\n')
#    except BaralhoException: #4º colocamos a classe de erro aqui e concluimos.
#        print('Fim!!! Baralho vázio')
#        break

print("Bem-vindo à guerra, vamos entrar no nosso jogo... \n")
# Criando baralho e dividindo em para duas pessoas embaralhadas
d= Baralho()
print(f'Quantidade de cartas: {len(d)}')
print(d)
d.shuffle()
mão1,mão2=d.dividir_cartas()

#Criando dois jogadores
jogador2 = Jogador("Computador",Mão(mão2))
nome=input("Digite seu nome: ")
jogador1 = Jogador(nome,Mão(mão1))

#print(f'Cartas do {jogador2.nome}: {str(jogador2.mao.x)}')
#print('\n')
#print(f'Cartas do {jogador1.nome}: {str(jogador1.mao.x)}')
#print('\n')

#Contadores:
total_rounds = 0
contagem_de_empates = 0

#fazendo o jogo andar (TESTE):
for i in range (13):
    input()
    total_rounds += 1  
    print("Aqui está a classificação atual:")
    print(jogador2.nome + " tem: "+str(len(jogador2.mao.x)))
    print(jogador1.nome + " tem: "+str(len(jogador1.mao.x)))
    print('\n')
    print("Hora de uma nova rodada!!! \n")
    print("Jogue uma carta!")

    table_cards = []

    c_carta = jogador2.carta_do_jogador()
    p_carta = jogador1.carta_do_jogador()
    table_cards.append(c_carta)
    table_cards.append(p_carta)

    if c_carta[0] == p_carta[0]:
        contagem_de_empates += 1
        print("EMPATE!!!")
        print(table_cards)
        table_cards.extend(jogador2.pegar_carta())
        table_cards.extend(jogador1.pegar_carta())

    if jogador2.mao.x.index(c_carta[0]) < jogador1.mao.x.index(p_carta[0]):
        jogador1.mao.adicionar_carta(table_cards)
    else:
        jogador2.mao.adicionar_carta(table_cards)
    
    if jogador1.mao.x.index(c_carta[0]) < jogador2.mao.x.index(p_carta[0]):
        jogador2.mao.adicionar_carta(table_cards)
    else:
        jogador1.mao.adicionar_carta(table_cards)

print("Game over,número de rodadas:"+str(total_rounds))
print("Uma guerra aconteceu: " + str(contagem_de_empates) +" vezes")
print("O computador ainda tem cartas?\t",str(jogador2.tem_carta()))
print("O jogador Humano ainda tem cartas?\t:",str(jogador1.tem_carta()))