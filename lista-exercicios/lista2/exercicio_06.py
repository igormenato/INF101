def verificar_numero(numero):
    if numero >= 100:
        return "O número é maior ou igual a 100."
    elif numero >= 51 and numero <= 99:
        return "O número está entre 51 e 99."
    else:
        return "O número é menor ou igual a 50."


def main():
    numero = float(input("Digite um número real: "))
    resultado = verificar_numero(numero)
    print(resultado)


if __name__ == "__main__":
    main()
