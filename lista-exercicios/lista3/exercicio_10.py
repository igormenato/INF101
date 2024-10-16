import os

precos = {1: 2.98, 2: 4.50, 3: 9.98, 4: 4.49, 5: 6.87}


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def exibir_menu():
    print("\n=== MENU ===")
    print("1. Adicionar venda")
    print("2. Ver resumo de vendas")
    print("3. Ver produtos vendidos")
    print("4. Sair\n")


def adicionar_venda(total_varejo, quantidades_vendidas, produtos_vendidos):
    limpar_tela()
    print("=== Adicionar Venda ===")
    while True:
        try:
            numero_produto = int(input("Digite o número do produto (1-5): "))
            if numero_produto not in precos:
                print("Número de produto inválido! Tente novamente.")
                continue
            quantidade_vendida = int(input("Digite a quantidade vendida: "))
            if quantidade_vendida <= 0:
                print("Quantidade inválida! Tente novamente.")
                continue
            break
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")

    preco_varejo = precos[numero_produto]
    valor_venda = preco_varejo * quantidade_vendida
    total_varejo += valor_venda
    quantidades_vendidas[numero_produto] = (
        quantidades_vendidas.get(numero_produto, 0) + quantidade_vendida
    )
    produtos_vendidos.append((numero_produto, quantidade_vendida))

    print("\nVenda registrada com sucesso!")
    print(f"Produto: {numero_produto}")
    print(f"Preço de varejo: ${preco_varejo:.2f}")
    print(f"Quantidade vendida: {quantidade_vendida}")
    print(f"Valor desta venda: ${valor_venda:.2f}")
    print(f"Total acumulado: ${total_varejo:.2f}")
    input("\nPressione Enter para continuar...")
    return total_varejo


def exibir_resumo(total_varejo, quantidades_vendidas):
    limpar_tela()
    print("=== Resumo de Vendas ===")
    print(f"Valor total a varejo: ${total_varejo:.2f}")
    print("\nQuantidades vendidas de cada produto:")

    # Ordenar os produtos
    for produto in sorted(precos.keys()):
        quantidade = quantidades_vendidas.get(produto, 0)
        valor = precos[produto] * quantidade
        print(f"Produto {produto}: {quantidade} unidades - ${valor:.2f}")

    input("\nPressione Enter para continuar...")


def exibir_produtos_vendidos(produtos_vendidos):
    limpar_tela()
    print("=== Produtos Vendidos ===")
    for i, (produto, quantidade) in enumerate(produtos_vendidos, 1):
        print(
            f"Venda {i}: Produto {produto} - {quantidade} unidades - ${precos[produto] * quantidade:.2f}"
        )
    input("\nPressione Enter para continuar...")


def main():
    total_varejo = 0
    quantidades_vendidas = {}
    produtos_vendidos = []

    while True:
        limpar_tela()
        exibir_menu()
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            total_varejo = adicionar_venda(
                total_varejo, quantidades_vendidas, produtos_vendidos
            )
        elif escolha == "2":
            exibir_resumo(total_varejo, quantidades_vendidas)
        elif escolha == "3":
            exibir_produtos_vendidos(produtos_vendidos)
        elif escolha == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("Pressione Enter para continuar...")


if __name__ == "__main__":
    main()
