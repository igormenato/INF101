def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def main():
    operador = input("Digite um operador matemático (+, -, *, /): ")
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    if operador == "+":
        resultado = somar(num1, num2)
    elif operador == "-":
        resultado = subtrair(num1, num2)
    elif operador == "*":
        resultado = multiplicar(num1, num2)
    elif operador == "/":
        resultado = dividir(num1, num2)
    else:
        print("Operador inválido!")

    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
