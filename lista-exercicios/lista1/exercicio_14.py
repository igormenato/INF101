def calcular_potencia_iluminacao(largura, comprimento):
    area = largura * comprimento

    potencia_por_m2 = 18

    potencia_total = area * potencia_por_m2

    return area, potencia_total


def main():
    largura = float(input("Digite a largura do cômodo em metros: "))
    comprimento = float(input("Digite o comprimento do cômodo em metros: "))

    area, potencia_total = calcular_potencia_iluminacao(largura, comprimento)

    print(f"A área do cômodo é: {area:.2f} m²")
    print(f"A potência de iluminação necessária é: {potencia_total:.2f} W")


if __name__ == "__main__":
    main()
