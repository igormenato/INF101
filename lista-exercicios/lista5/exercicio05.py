def main():
    A = []
    B = []

    print("Digite os 10 elementos do vetor A:")
    for i in range(10):
        num = int(input(f"Digite o {i+1}º número do vetor A: "))
        A.append(num)

    print("\nDigite os 10 elementos do vetor B:")
    for i in range(10):
        num = int(input(f"Digite o {i+1}º número do vetor B: "))
        B.append(num)

    vetor_intercalado = []
    for i in range(10):
        vetor_intercalado.append(A[i])
        vetor_intercalado.append(B[i])

    print("\nVetor intercalado:")
    print(vetor_intercalado)


if __name__ == "__main__":
    main()
