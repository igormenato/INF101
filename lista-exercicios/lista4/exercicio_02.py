def calcular_potencia(x, n):
    resultado = 1
    while n > 0:
        resultado *= x
        n -= 1
    return resultado


def main():
    x = int(input("Digite o valor de x: "))
    n = int(input("Digite o valor de n: "))

    potencia = calcular_potencia(x, n)
    print(f"{x} elevado a {n} é igual a {potencia}")


if __name__ == "__main__":
    main()
