def verifica_par_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"


def verifica_positivo_negativo(numero):
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "zero"


def main():
    try:
        numero = int(input("Digite um número inteiro: "))

        resultado_par_impar = verifica_par_impar(numero)
        resultado_pos_neg = verifica_positivo_negativo(numero)

        print(f"O número {numero} é {resultado_par_impar} e {resultado_pos_neg}.")

    except ValueError:
        print("Por favor, digite um número inteiro válido.")


if __name__ == "__main__":
    main()
