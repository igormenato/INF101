def ler_valores():
    y = float(input("Digite o valor de y: "))
    z = float(input("Digite o valor de z: "))
    return y, z


def calcular_x(y, z):
    if z == 0:
        raise ValueError("O valor de z não pode ser zero.")
    x = ((3 * y) * (y + z)) / z
    return x


def main():
    y, z = ler_valores()
    try:
        x = calcular_x(y, z)
        print(f"O valor de x é: {x}")
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
