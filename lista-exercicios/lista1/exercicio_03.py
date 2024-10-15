def calcular_media_aritmetica(num1, num2):
    return (num1 + num2) / 2


def main():
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        media = calcular_media_aritmetica(num1, num2)
        print(f"A média aritmética entre {num1} e {num2} é {media}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")


if __name__ == "__main__":
    main()
