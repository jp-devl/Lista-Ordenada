def insere(codigo, t, tamanho):
    if t[0] == tamanho:
        print("\nAtenção! Lista cheia\n")
    else:
        prod = int(input("\nDigite código do produto a ser inserido: "))
        codigo[t[0]] = prod
        t[0] += 1

def exibe(codigo, t):
    if t == 0:
        print("\nAtenção! Lista vazia\n")
    else:
        print("\nRelação dos códigos")
        for x in range(t):
            print(f"{x+1} - {codigo[x]}")

def elemento(codigo, t):
    if t == 0:
        print("\nAtenção! Lista vazia\n")
        return
    posicao = abs(int(input("\nQual a posição que deseja?: "))) - 1
    if posicao >= t:
        print("\nAtenção! Nenhum código armazenado ou posição inexistente\n")
    else:
        print(f"\nCódigo na posição: {codigo[posicao]}\n")

def ordena(codigo, t):
    if t == 0:
        print("\nAtenção! Lista vazia\n")
    else:
        for x in range(t - 1):
            aux = x
            for y in range(x + 1, t):
                if codigo[aux] > codigo[y]:
                    aux = y
            codigo[x], codigo[aux] = codigo[aux], codigo[x]
        print("\nLista Ordenada\n")

def buscar_sequencial(codigo, cod, t):
    if t == 0:
        return -1  
    for x in range(t):
        if codigo[x] == cod:
            return x  
    return -2  