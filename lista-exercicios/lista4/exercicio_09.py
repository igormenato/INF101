def encontrar_maior_menor(n):
    maior = float("-inf")
    menor = float("inf")

    while n > 0:
        numero = int(input("Digite um número: "))
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
        n -= 1

    return maior, menor


def main():
    n = int(input("Digite a quantidade de números a serem lidos: "))
    maior, menor = encontrar_maior_menor(n)
    print(f"O maior número é: {maior}")
    print(f"O menor número é: {menor}")


if __name__ == "__main__":
    main()
