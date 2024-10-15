def verificar_codigo(codigo):
    if codigo == 1:
        return "Grupo com 50% de promoção"
    elif codigo == 3 or codigo == 5:
        return "Grupo sem desconto"
    elif codigo >= 10 and codigo <= 20:
        return "Grupo com 10% de desconto"
    else:
        return "Código não válido"


def main():
    codigo = int(input("Digite o código: "))
    mensagem = verificar_codigo(codigo)
    print(mensagem)


if __name__ == "__main__":
    main()
