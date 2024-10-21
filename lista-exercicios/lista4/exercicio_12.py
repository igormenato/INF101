def contar_numeros_pares_impares():
    n = int(input("Digite a quantidade de números a serem informados: "))
    numeros_pares = 0
    numeros_impares = 0

    while n > 0:
        numero = int(input("Digite um número inteiro: "))
        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
        n -= 1

    return numeros_pares, numeros_impares


def main():
    numeros_pares, numeros_impares = contar_numeros_pares_impares()
    print("Quantidade de números pares:", numeros_pares)
    print("Quantidade de números ímpares:", numeros_impares)


if __name__ == "__main__":
    main()
