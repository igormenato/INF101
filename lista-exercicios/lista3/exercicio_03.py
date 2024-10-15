import math


def calcular(opcao, numero):
    resultado = None

    match opcao:
        case 1:
            resultado = math.sqrt(numero)
        case 2:
            resultado = numero / 2
        case 3:
            resultado = numero * 0.1
        case 4:
            resultado = numero * 2
        case _:
            print("Opção inválida!")

    return resultado


def exibir_menu():
    print("Menu:")
    print("1 - Raiz quadrada")
    print("2 - A metade")
    print("3 - 10% do número")
    print("4 - O dobro")


def main():
    exibir_menu()
    opcao = int(input("Digite a opção desejada: "))
    numero = float(input("Digite um número: "))

    resultado = calcular(opcao, numero)
    print("Resultado:", resultado)


if __name__ == "__main__":
    main()
