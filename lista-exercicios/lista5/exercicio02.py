def main():
    vetor = []

    print("Digite 10 números inteiros:")
    for i in range(10):
        numero = int(input(f"Digite o {i+1}º número: "))
        vetor.append(numero)

    print("\nValores do vetor:")
    for i in range(10):
        if vetor[i] % 2 == 0:
            vetor[i] += 10
        print(f"Posição {i}: {vetor[i]}")


if __name__ == "__main__":
    main()
