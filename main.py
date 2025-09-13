from menu import mostrar_menu, ler_opcao
import acoes

def main():
    TAMANHO = 5
    codigoProduto = [0] * TAMANHO
    tam = [0]
    op = -1

    funcoes = [
        acoes.zerar_lista,
        acoes.inserir_produto,
        acoes.exibir_lista,
        acoes.mostrar_tamanho,
        acoes.mostrar_elemento,
        acoes.ordenar_lista,
        acoes.buscar_codigo,
        acoes.sair
    ]

    while op != 7:
        mostrar_menu()
        op = ler_opcao()
        if 0 <= op < len(funcoes):
            funcoes[op](codigoProduto, tam, TAMANHO)
        else:
            print("\nOpção inválida\n")

if __name__ == "__main__":
    main()