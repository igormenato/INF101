def calcular_fatorial(numero):
    fatorial = 1
    while numero > 1:
        fatorial *= numero
        numero -= 1
    return fatorial


def main():
    numero = int(input("Digite um número inteiro: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}.")


if __name__ == "__main__":
    main()
