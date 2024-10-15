def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) / 1.8


def main():
    try:
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        celsius = fahrenheit_para_celsius(fahrenheit)
        print(f"A temperatura em Celsius é: {celsius:.2f}")
    except ValueError:
        print("Por favor, insira um valor numérico válido.")


if __name__ == "__main__":
    main()
