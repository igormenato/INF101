import math


def calcular_area(raio):
    return math.pi * raio**2


def calcular_volume(raio, altura):
    return math.pi * raio**2 * altura


def main():
    altura = float(input("Digite a altura do cilindro: "))
    raio = float(input("Digite o raio do cilindro: "))

    area = calcular_area(raio)
    volume = calcular_volume(raio, altura)

    print(f"Área da base do cilindro: {area:.2f}")
    print(f"Volume do cilindro: {volume:.2f}")


if __name__ == "__main__":
    main()
