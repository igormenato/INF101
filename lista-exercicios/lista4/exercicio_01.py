class Exercicio01:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        return a / b

    @staticmethod
    def main():
        operador = input("Digite um operador matemático (+, -, *, /): ")
        while operador not in ["+", "-", "*", "/"]:
            print("Operador inválido!")
            operador = input("Digite um operador matemático (+, -, *, /): ")
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))

        if operador == "+":
            resultado = Exercicio01.somar(num1, num2)
        elif operador == "-":
            resultado = Exercicio01.subtrair(num1, num2)
        elif operador == "*":
            resultado = Exercicio01.multiplicar(num1, num2)
        elif operador == "/":
            resultado = Exercicio01.dividir(num1, num2)

        print("Resultado:", resultado)


class Exercicio02:
    @staticmethod
    def somar(a, b):
        return a + b

    @staticmethod
    def subtrair(a, b):
        return a - b

    @staticmethod
    def multiplicar(a, b):
        return a * b

    @staticmethod
    def dividir(a, b):
        return a / b

    @staticmethod
    def main():
        operador = input("Digite um operador matemático (+, -, *, /): ")
        while operador not in ["+", "-", "*", "/"]:
            print("Operador inválido!")
            operador = input("Digite um operador matemático (+, -, *, /): ")
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

        resultado = None

        # Requer Python 3.10 ou superior
        match operador:
            case "+":
                resultado = Exercicio02.somar(numero1, numero2)
            case "-":
                resultado = Exercicio02.subtrair(numero1, numero2)
            case "*":
                resultado = Exercicio02.multiplicar(numero1, numero2)
            case "/":
                resultado = Exercicio02.dividir(numero1, numero2)

        if resultado is not None:
            print("Resultado:", resultado)


def main():
    while True:
        print("\nSelecione qual exercício rodar:")
        print("1. Exercicio 01")
        print("2. Exercicio 02")
        print("0. Sair")

        choice = input("Digite sua escolha: ").strip().lower()

        if choice == "1":
            print("Executando Exercicio 01")
            Exercicio01.main()
        elif choice == "2":
            print("Executando Exercicio 02")
            Exercicio02.main()
        elif choice == "0":
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.")

        repeat = input("Deseja repetir a operação? (0 - Não, 1 - Sim): ")
        if repeat == "0":
            print("Saindo...")
            break


if __name__ == "__main__":
    main()
