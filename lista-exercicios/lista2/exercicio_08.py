def verificar_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


def verificar_positivo_negativo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"


def main():
    numero = int(input("Digite um número inteiro: "))
    par_impar = verificar_par_impar(numero)
    positivo_negativo = verificar_positivo_negativo(numero)
    print(f"O número {numero} é {par_impar} e {positivo_negativo}.")


if __name__ == "__main__":
    main()
