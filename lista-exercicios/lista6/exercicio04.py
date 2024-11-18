import random


def gerar_matriz(ordem):
    matriz = []
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            linha.append(random.randint(0, 100))
        matriz.append(linha)
    return matriz


def obter_diagonal_secundaria(matriz):
    diagonal = []
    ordem = len(matriz)
    for i in range(ordem):
        diagonal.append(matriz[i][ordem - 1 - i])
    return diagonal


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
        print()


def main():
    ordem = 5
    print("Gerando matriz aleatória 5x5:")
    matriz = gerar_matriz(ordem)
    imprimir_matriz(matriz)

    print("\nElementos da diagonal secundária:")
    diagonal_sec = obter_diagonal_secundaria(matriz)
    print(diagonal_sec)


if __name__ == "__main__":
    main()
