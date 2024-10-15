def dividir_por_dois(x):
    return x / 2


def main():
    try:
        x = float(input("Digite um número: "))
        resultado = dividir_por_dois(x)
        print(f"O resultado da divisão de {x} por 2 é {resultado}")
    except ValueError:
        print("Por favor, insira um número válido.")


if __name__ == "__main__":
    main()
