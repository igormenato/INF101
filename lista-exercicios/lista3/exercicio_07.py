def classificar_atleta(nome, idade):
    nome = nome.capitalize()  # Primeira letra sempre maiúscula
    if idade >= 5 and idade <= 10:
        categoria = "Infantil"
    elif idade >= 11 and idade <= 15:
        categoria = "Juvenil"
    elif idade >= 16 and idade <= 20:
        categoria = "Junior"
    elif idade >= 21 and idade <= 25:
        categoria = "Profissional"
    else:
        categoria = "Categoria não encontrada"

    print(f"O atleta {nome} está na categoria {categoria}")


def main():
    nome = input("Digite o nome do atleta: ")
    idade = int(input("Digite a idade do atleta: "))

    classificar_atleta(nome, idade)


if __name__ == "__main__":
    main()
