def verificar_numero(numero):
    if numero > 0:
        return "O número é positivo."
    elif numero < 0:
        return "O número é negativo."
    else:
        return "O número é igual a zero."


def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = verificar_numero(numero)
    print(f"O número é {resultado}.")


if __name__ == "__main__":
    main()
