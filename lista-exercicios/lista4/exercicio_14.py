def calcular_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    print("-" * 15)

    for contador in range(1, 11):
        resultado = numero * contador
        print(f"{numero:2} x {contador:2} = {resultado:3}")

    print("-" * 15)


def obter_numero():
    while True:
        try:
            numero = int(input("Digite um número (1-100): "))
            if 1 <= numero <= 100:
                return numero
            print("Por favor, digite um número entre 1 e 100.")
        except ValueError:
            print("Entrada inválida. Digite apenas números inteiros.")


def main():
    numero = obter_numero()
    calcular_tabuada(numero)


if __name__ == "__main__":
    main()
