def calcular_desconto(idade):
    valor_passagem = 100.00
    desconto = 0.00

    if idade > 65 or idade < 18:
        desconto = 20.00
        valor_passagem -= desconto

    return valor_passagem, desconto


def main():
    idade = int(input("Informe sua idade: "))

    valor_passagem, desconto = calcular_desconto(idade)

    if desconto > 0:
        print("Foi aplicado um desconto de R$ {:.2f}.".format(desconto))
    else:
        print("Não foi possível aplicar nenhum desconto.")

    print("Valor a ser pago pela passagem: R$ {:.2f}.".format(valor_passagem))


if __name__ == "__main__":
    main()
