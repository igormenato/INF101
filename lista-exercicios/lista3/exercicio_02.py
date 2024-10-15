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
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))

    resultado = None

    # Na versão 3.10 do Python, foi introduzido o match case, equivalente ao switch case em C, por exemplo.
    match operador:
        case "+":
            resultado = somar(numero1, numero2)
        case "-":
            resultado = subtrair(numero1, numero2)
        case "*":
            resultado = multiplicar(numero1, numero2)
        case "/":
            resultado = dividir(numero1, numero2)
        case _:
            print("Operador inválido!")

    if resultado is not None:
        print("Resultado:", resultado)


if __name__ == "__main__":
    main()
