def multiplicar(x, y):
    resultado = x * y
    print(f"O resultado da multiplicação é: {resultado}")


def main():
    x = float(input("Digite o primeiro número (x): "))
    y = float(input("Digite o segundo número (y): "))

    multiplicar(x, y)


if __name__ == "__main__":
    main()
