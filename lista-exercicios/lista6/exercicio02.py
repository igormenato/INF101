import random


def preencher_matriz():
    matriz = []
    for i in range(5):
        linha = []
        for j in range(5):
            linha.append(random.randint(0, 100))
        matriz.append(linha)
    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
        print()


def main():
    print("Gerando matriz 5x5 com números aleatórios:")
    matriz = preencher_matriz()
    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()
