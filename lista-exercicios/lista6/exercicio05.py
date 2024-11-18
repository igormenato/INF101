import random


def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(random.randint(0, 100))
        matriz.append(linha)
    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
        print()


def somar_linhas(matriz):
    somas = []
    for linha in matriz:
        somas.append(sum(linha))
    return somas


def main():
    matriz = criar_matriz(7, 5)

    print("Matriz gerada:")
    imprimir_matriz(matriz)

    somas = somar_linhas(matriz)
    print("\nSoma de cada linha:")
    for i, soma in enumerate(somas):
        print(f"Linha {i + 1}: {soma}")


if __name__ == "__main__":
    main()
