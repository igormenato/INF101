def main():
    vetor = []

    print("Digite 10 números inteiros:")
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        vetor.append(numero)

    print("\nNúmeros digitados:")
    for i, numero in enumerate(vetor):
        print(f"Posição {i}: {numero}")


if __name__ == "__main__":
    main()
