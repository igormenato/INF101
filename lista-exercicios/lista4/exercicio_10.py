def encontrar_maior_menor(n):
    maior = float("-inf")
    menor = float("inf")

    for i in range(n):
        num = int(input("Digite um número inteiro: "))

        if num > maior:
            maior = num

        if num < menor:
            menor = num

    return maior, menor


def main():
    n = int(input("Digite a quantidade de números a serem lidos: "))
    maior, menor = encontrar_maior_menor(n)
    print(f"O maior número informado é: {maior}")
    print(f"O menor número informado é: {menor}")


if __name__ == "__main__":
    main()
