import random


def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(0, 100))
        matriz.append(linha)
    return matriz


def somar_colunas(matriz):
    somas = []
    for j in range(len(matriz[0])):
        soma = 0
        for i in range(len(matriz)):
            soma += matriz[i][j]
        somas.append(soma)
    return somas


def exibir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
        print()


def main():
    print("Matriz gerada:")
    matriz = criar_matriz(7, 5)
    exibir_matriz(matriz)

    somas = somar_colunas(matriz)

    print("\nSoma de cada coluna:")
    for i, soma in enumerate(somas):
        print(f"Coluna {i + 1}: {soma}")


if __name__ == "__main__":
    main()
