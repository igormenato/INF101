def calcular_S():
    S = 0
    numerador = 1
    denominador = 1

    while numerador <= 99 and denominador <= 50:
        S += numerador / denominador
        numerador += 2
        denominador += 1

    return S


def main():
    valor_S = calcular_S()
    print(f"O valor de S é: {valor_S}")


if __name__ == "__main__":
    main()
