def criar_matriz():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(i * j)
        matriz.append(linha)
    return matriz


def imprimir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:3d}", end=" ")
        print()


def main():
    print("Matriz 10x10 com o produto dos índices:")
    matriz = criar_matriz()
    imprimir_matriz(matriz)


if __name__ == "__main__":
    main()
