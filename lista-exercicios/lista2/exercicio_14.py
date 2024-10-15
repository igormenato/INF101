def ordenar_numeros(x, y, ordem):
    if ordem == 1:
        if x > y:
            return y, x
        else:
            return x, y
    elif ordem == 2:
        if x < y:
            return y, x
        else:
            return x, y
    else:
        print("Opção inválida!")


def main():
    x = int(input("Digite o primeiro número: "))
    y = int(input("Digite o segundo número: "))
    ordem = int(input("Escolha a ordem (1 - crescente, 2 - decrescente): "))

    resultado = ordenar_numeros(x, y, ordem)
    print("Os números ordenados são:", resultado[0], "e", resultado[1])


if __name__ == "__main__":
    main()
