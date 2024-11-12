def main():
    vetor = []

    for i in range(10):
        valor = int(input(f"Digite o {i+1}º número inteiro: "))
        vetor.append(valor)

    print("\nNúmeros em ordem inversa multiplicados por 2:")

    for i in range(len(vetor) - 1, -1, -1):
        print(f"{vetor[i] * 2}")


if __name__ == "__main__":
    main()
