def calcular_salario_total(salario_fixo, valor_vendas, percentual_comissao):
    return salario_fixo + (valor_vendas * (percentual_comissao / 100))


def main():
    id_vendedor = input("Digite o ID do vendedor: ")
    salario_fixo = float(input("Digite o salário fixo do vendedor: "))
    valor_vendas = float(input("Digite o valor das vendas efetuadas pelo vendedor: "))
    percentual_comissao = float(
        input("Digite o percentual de comissão sobre as vendas: ")
    )

    salario_total = calcular_salario_total(
        salario_fixo, valor_vendas, percentual_comissao
    )

    print(f"ID do Vendedor: {id_vendedor}")
    print(f"Salário Total: R$ {salario_total:.2f}")


if __name__ == "__main__":
    main()
