def calcular_volume_caixa(comprimento, largura, altura):
    return comprimento * largura * altura


def main():
    try:
        comprimento = float(input("Informe o comprimento da caixa: "))
        largura = float(input("Informe a largura da caixa: "))
        altura = float(input("Informe a altura da caixa: "))

        volume = calcular_volume_caixa(comprimento, largura, altura)
        print(f"O volume da caixa retangular é: {volume} unidades cúbicas")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")


if __name__ == "__main__":
    main()
