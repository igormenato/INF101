# Dicionário com os preços de varejo dos produtos
precos = {1: 2.98, 2: 4.50, 3: 9.98, 4: 4.49, 5: 6.87}

# Variável para armazenar o valor total a varejo
total_varejo = 0

# Dicionário para armazenar as quantidades vendidas de cada produto
quantidades_vendidas = {}

# Lista para armazenar os produtos vendidos
produtos_vendidos = []

# Loop para ler os pares de números
while True:
    numero_produto = int(input("Digite o número do produto (ou 0 para sair): "))
    if numero_produto == 0:
        break
    quantidade_vendida = int(input("Digite a quantidade vendida: "))

    # Verifica se o número do produto existe no dicionário
    if numero_produto in precos:
        preco_varejo = precos[numero_produto]
        total_varejo += preco_varejo * quantidade_vendida
        quantidades_vendidas[numero_produto] = (
            quantidades_vendidas.get(numero_produto, 0) + quantidade_vendida
        )
        produtos_vendidos.append((numero_produto, quantidade_vendida))
        print("Produto:", numero_produto)
        print("Preço de varejo:", preco_varejo)
        print("Quantidade vendida:", quantidade_vendida)
        print("Valor total a varejo:", total_varejo)
        print()  # Print an empty line for separation
    else:
        print("Número de produto inválido!")

# Exibe o valor total a varejo
print(
    "O valor total a varejo de todos os produtos vendidos na semana passada é:",
    total_varejo,
)

# Exibe as quantidades vendidas de cada produto
print("Quantidades vendidas de cada produto:")
for produto, quantidade in quantidades_vendidas.items():
    print("Produto:", produto)
    print("Quantidade vendida:", quantidade)
    print()  # Print an empty line for separation

# Exibe os produtos vendidos
print("Produtos vendidos:")
for produto, quantidade in produtos_vendidos:
    print("Produto:", produto)
    print("Quantidade vendida:", quantidade)
    print()  # Print an empty line for separation
