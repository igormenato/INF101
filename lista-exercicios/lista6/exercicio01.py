def main():
    matriz = []

    print("Digite os valores para a matriz 3x3:")
    for i in range(3):
        linha = []
        for j in range(3):
            valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
            linha.append(valor)
        matriz.append(linha)

    print("\nMatriz preenchida:")
    for linha in matriz:
        for valor in linha:
            print(f"{valor:3d}", end=" ")
        print()


if __name__ == "__main__":
    main()
