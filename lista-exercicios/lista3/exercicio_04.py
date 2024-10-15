def menu():
    print("Menu:")
    print("1 - Venda a Vista")
    print("2 - Venda a Prazo 30 dias")
    print("3 - Venda a Prazo 60 dias")
    print("4 - Venda a Prazo 90 dias")
    print("5 - Venda com cartão de débito")
    print("6 - Venda com cartão de crédito")


def calcular_desconto(valor, desconto):
    return valor - (valor * desconto / 100)


def calcular_acrescimo(valor, acrescimo):
    return valor + (valor * acrescimo / 100)


def calcular_total_venda(valor, opcao):
    match opcao:
        case 1:
            return calcular_desconto(valor, 10)
        case 2:
            return calcular_desconto(valor, 5)
        case 3:
            return valor
        case 4:
            return calcular_acrescimo(valor, 5)
        case 5:
            return calcular_desconto(valor, 8)
        case 6:
            return calcular_desconto(valor, 7)
        case _:
            return "Opção inválida"


def main():
    menu()
    valor_venda = float(input("Digite o valor da venda: "))
    opcao = int(input("Digite o número da opção desejada: "))

    total_venda = calcular_total_venda(valor_venda, opcao)
    print("Total da venda: R$", total_venda)


if __name__ == "__main__":
    main()
