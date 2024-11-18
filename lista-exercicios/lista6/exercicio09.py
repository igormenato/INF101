import random


def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(0, 100))
        matriz.append(linha)
    return matriz


def somar_matrizes(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    matriz_soma = []

    for i in range(linhas):
        linha = []
        for j in range(colunas):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        matriz_soma.append(linha)
    return matriz_soma


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:4d}", end=" ")
        print()


def main():
    linhas = 3
    colunas = 3

    print("Matriz 1:")
    matriz1 = criar_matriz(linhas, colunas)
    imprimir_matriz(matriz1)

    print("\nMatriz 2:")
    matriz2 = criar_matriz(linhas, colunas)
    imprimir_matriz(matriz2)

    print("\nSoma das matrizes:")
    matriz_soma = somar_matrizes(matriz1, matriz2)
    imprimir_matriz(matriz_soma)


if __name__ == "__main__":
    main()
