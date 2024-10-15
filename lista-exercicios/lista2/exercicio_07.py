def verificar_positivo_negativo(num1, num2):
    if num1 > 0 and num2 > 0:
        return "POSITIVO"
    elif num1 < 0 and num2 < 0:
        return "NEGATIVO"
    else:
        return "POSITIVO E NEGATIVO"


def main():
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))

    resultado = verificar_positivo_negativo(num1, num2)
    print(resultado)


if __name__ == "__main__":
    main()
