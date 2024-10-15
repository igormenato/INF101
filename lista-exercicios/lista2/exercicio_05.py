def verificar_numero(numero):
    if numero >= 10:
        return "O número é maior ou igual a 10."
    else:
        return "O número é menor do que 10."


def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = verificar_numero(numero)
    print(resultado)


if __name__ == "__main__":
    main()
