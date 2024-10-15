def estado_civil(letra):
    # Aceita tanto maiúsculas quanto minúsculas
    letra = letra.lower()
    estados_civis = {
        "s": "Solteiro",
        "c": "Casado",
        "v": "Viúvo",
        "d": "Divorciado",
        "q": "Desquitado",
    }
    return estados_civis.get(letra, "Estado civil inválido")


def main():
    letra_estado_civil = input("Digite a primeira letra do estado civil: ")
    descricao_estado_civil = estado_civil(letra_estado_civil)
    print(descricao_estado_civil)


if __name__ == "__main__":
    main()
