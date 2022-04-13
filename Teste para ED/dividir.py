lista = [*range(1, 100, 1)]
print(lista)
def listasMenores(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
        
listasDivididas = list(listasMenores(lista, 5))
print(listasDivididas)