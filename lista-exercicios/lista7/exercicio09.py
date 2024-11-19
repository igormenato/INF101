def calcular_valor_final(valor_venda, condicao):
    if condicao == 1:
        return valor_venda * 0.9  # 10% desconto
    elif condicao == 2:
        return valor_venda * 0.95  # 5% desconto
    elif condicao == 3:
        return valor_venda  # mesmo preço
    elif condicao == 4:
        return valor_venda * 1.05  # 5% acréscimo
    elif condicao == 5:
        return valor_venda * 0.92  # 8% desconto
    elif condicao == 6:
        return valor_venda * 0.93  # 7% desconto
    else:
        return None


def exibir_menu():
    print("\nCondições de Pagamento:")
    print("1 - Venda a Vista - desconto de 10%")
    print("2 - Venda a Prazo 30 dias - desconto de 5%")
    print("3 - Venda a Prazo 60 dias - mesmo preço")
    print("4 - Venda a Prazo 90 dias - acréscimo de 5%")
    print("5 - Venda com cartão de débito - desconto de 8%")
    print("6 - Venda com cartão de crédito - desconto de 7%")


def main():
    try:
        valor_venda = float(input("Digite o valor da venda: R$ "))
        exibir_menu()
        condicao = int(input("Escolha a condição de pagamento (1-6): "))

        valor_final = calcular_valor_final(valor_venda, condicao)

        if valor_final is not None:
            print(f"\nValor original da venda: R$ {valor_venda:.2f}")
            print(f"Valor final da venda: R$ {valor_final:.2f}")
        else:
            print("Opção de pagamento inválida!")

    except ValueError:
        print("Erro: Digite apenas números!")


if __name__ == "__main__":
    main()
