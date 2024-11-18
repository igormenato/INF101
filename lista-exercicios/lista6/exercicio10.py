import random


def criar_matriz(ordem):
    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(random.randint(0, 100))
        matriz.append(linha)
    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:4d}", end=" ")
        print()


def soma_abaixo_diagonal(matriz):
    soma = 0
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if i > j:
                soma += matriz[i][j]
    return soma


def main():
    ordem = 5
    print("Gerando matriz {}x{}...".format(ordem, ordem))
    matriz = criar_matriz(ordem)

    print("\nMatriz gerada:")
    imprimir_matriz(matriz)

    soma = soma_abaixo_diagonal(matriz)
    print("\nA soma dos elementos abaixo da diagonal principal é:", soma)


if __name__ == "__main__":
    main()
