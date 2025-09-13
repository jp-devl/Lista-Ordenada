from lista import insere, exibe, elemento, ordena, buscar_sequencial

def zerar_lista(codigoProduto, tam, TAMANHO):
    tam[0] = 0
    input("\nPressione ENTER para continuar...")

def inserir_produto(codigoProduto, tam, TAMANHO):
    insere(codigoProduto, tam, TAMANHO)
    input("\nPressione ENTER para continuar...")

def exibir_lista(codigoProduto, tam, TAMANHO):
    exibe(codigoProduto, tam[0])
    input("\nPressione ENTER para continuar...")

def mostrar_tamanho(codigoProduto, tam, TAMANHO):
    print(f"\nTamanho da Lista: {tam[0]}")
    input("\nPressione ENTER para continuar...")

def mostrar_elemento(codigoProduto, tam, TAMANHO):
    elemento(codigoProduto, tam[0])
    input("\nPressione ENTER para continuar...")

def ordenar_lista(codigoProduto, tam, TAMANHO):
    ordena(codigoProduto, tam[0])
    input("\nPressione ENTER para continuar...")

def buscar_codigo(codigoProduto, tam, TAMANHO):
    cod = int(input("\nQual código a ser procurado? "))
    posicao = buscar_sequencial(codigoProduto, cod, tam[0])
    if posicao == -1:
        print("\nAtenção! Lista vazia\n")
    elif posicao == -2:
        print("\nAtenção! Código não encontrado\n")
    else:
        print(f"\nCódigo encontrado na posição: {posicao+1}\n")
    input("\nPressione ENTER para continuar...")

def sair(codigoProduto, tam, TAMANHO):
    print("\nFinalizando o programa da LISTA\n")
    input("\nPressione ENTER para continuar...")