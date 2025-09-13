def mostrar_menu():
    print("\nMenu - Lista")
    print("\n0 - Reiniciar a LISTA")
    print("1 - Inserir código na LISTA")
    print("2 - Exibir LISTA")
    print("3 - Exibir tamanho da LISTA")
    print("4 - Exibir um elemento da LISTA")
    print("5 - Ordenar a LISTA")
    print("6 - Buscar código na LISTA")
    print("7 - Sair")

def ler_opcao():
    while True:
        try:
            return int(input("\nOpção: "))
        except ValueError:
            print("Digite apenas o número da opção!")