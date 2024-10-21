def divide_por_dois(numero):
    contador = 0
    while numero >= 1:
        numero /= 2
        contador += 1
    return numero, contador


def main():
    numero = float(input("Digite um número: "))
    resultado, quantidade_divisoes = divide_por_dois(numero)
    print("Última divisão:", resultado)
    print("Quantidade de divisões efetuadas:", quantidade_divisoes)


if __name__ == "__main__":
    main()
