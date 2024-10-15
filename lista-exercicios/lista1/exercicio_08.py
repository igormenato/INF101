def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


def main():
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    area = calcular_area_triangulo(base, altura)
    print(f"A área do triângulo é: {area}")


if __name__ == "__main__":
    main()
