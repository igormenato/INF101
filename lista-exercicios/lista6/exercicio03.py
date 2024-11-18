import random


def gerar_matriz(ordem):
    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(random.randint(0, 100))
        matriz.append(linha)
    return matriz


def obter_diagonal_principal(matriz):
    diagonal = []
    for i in range(len(matriz)):
        diagonal.append(matriz[i][i])
    return diagonal


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:3}", end=" ")
        print()


def main():
    ordem = 5

    print("Matriz gerada:")
    matriz = gerar_matriz(ordem)
    imprimir_matriz(matriz)

    diagonal = obter_diagonal_principal(matriz)
    print("\nElementos da diagonal principal:")
    print(diagonal)


if __name__ == "__main__":
    main()
