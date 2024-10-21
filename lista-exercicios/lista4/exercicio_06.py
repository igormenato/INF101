def calcular_soma(conjunto):
    soma = 0
    for elemento in conjunto:
        soma += elemento
    return soma


def calcular_media(conjunto):
    soma = calcular_soma(conjunto)
    media = soma / len(conjunto)
    return media


def main():
    x = int(input("Informe a quantidade de elementos: "))
    conjunto = []

    for i in range(x):
        elemento = float(input("Informe o elemento {}: ".format(i + 1)))
        conjunto.append(elemento)

    soma = calcular_soma(conjunto)
    media = calcular_media(conjunto)

    print("Soma: ", soma)
    print("Média: ", media)


if __name__ == "__main__":
    main()
