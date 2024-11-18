import random


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
        print()


def encontrar_maior_elemento(matriz):
    maior = matriz[0][0]
    linha_maior = 0
    coluna_maior = 0

    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] > maior:
                maior = matriz[i][j]
                linha_maior = i
                coluna_maior = j

    return maior, linha_maior, coluna_maior


def main():
    matriz = [[random.randint(0, 100) for j in range(5)] for i in range(7)]

    print("Matriz gerada:")
    imprimir_matriz(matriz)

    maior, linha, coluna = encontrar_maior_elemento(matriz)

    print(f"\nMaior elemento: {maior}")
    print(f"Posição: linha {linha}, coluna {coluna}")


if __name__ == "__main__":
    main()
