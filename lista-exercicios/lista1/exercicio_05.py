def main():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    soma = num1 + num2
    produto = num1 * num2
    divisao = num1 / num2 if num2 != 0 else "Divisão por zero não é permitida"
    subtracao = num1 - num2

    print(f"Soma: {soma}")
    print(f"Produto: {produto}")
    print(f"Divisão: {divisao}")
    print(f"Subtração: {subtracao}")


if __name__ == "__main__":
    main()
