def ler_conjunto():
    conjunto = []
    x = int(input("Informe a quantidade de elementos: "))
    for i in range(x):
        elemento = float(input("Informe o elemento {}: ".format(i + 1)))
        conjunto.append(elemento)
    return conjunto


def calcular_soma(conjunto):
    soma = sum(conjunto)
    return soma


def calcular_media(conjunto):
    media = sum(conjunto) / len(conjunto)
    return media


def main():
    conjunto = ler_conjunto()
    soma = calcular_soma(conjunto)
    media = calcular_media(conjunto)

    print("Soma: ", soma)
    print("Média: ", media)


if __name__ == "__main__":
    main()
