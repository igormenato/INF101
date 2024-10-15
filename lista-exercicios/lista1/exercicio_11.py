def main():
    produto1_nome = "Produto 1"
    produto1_valor = 10.0
    produto2_nome = "Produto 2"
    produto2_valor = 20.0

    quantidade_produto1 = int(
        input(f"Quantas unidades de {produto1_nome} você deseja obter? ")
    )
    quantidade_produto2 = int(
        input(f"Quantas unidades de {produto2_nome} você deseja obter? ")
    )

    valor_total = calcular_valor_total(
        quantidade_produto1, produto1_valor, quantidade_produto2, produto2_valor
    )

    print(f"O valor total da compra é: R${valor_total:.2f}")


def calcular_valor_total(
    quantidade_produto1, valor_produto1, quantidade_produto2, valor_produto2
):
    total_produto1 = quantidade_produto1 * valor_produto1
    total_produto2 = quantidade_produto2 * valor_produto2
    return total_produto1 + total_produto2


if __name__ == "__main__":
    main()
