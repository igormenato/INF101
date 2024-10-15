def main():
    try:
        numero = int(input("Digite um número inteiro: "))
        print(f"Você digitou: {numero}")
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")


if __name__ == "__main__":
    main()
