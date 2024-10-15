def calcular_preco_total(codigo, quantidade):
    tabela_precos = {1001: 5.32, 1324: 6.45, 6548: 2.37, 987: 5.32, 7623: 6.45}

    if codigo in tabela_precos:
        preco_unitario = tabela_precos[codigo]
        preco_total = preco_unitario * quantidade
        return preco_total
    else:
        return "Código inválido"


def main():
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade comprada: "))

    preco_total = calcular_preco_total(codigo, quantidade)
    print(f"Preço total: R$ {preco_total}")


if __name__ == "__main__":
    main()
