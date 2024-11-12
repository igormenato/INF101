def main():
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(len(vetor)):
        vetor[i] = vetor[i] * i

    print(vetor)


if __name__ == "__main__":
    main()
