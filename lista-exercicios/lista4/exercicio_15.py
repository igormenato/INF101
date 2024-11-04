def imprimir_tabuada(inicio=1, fim=5, multiplicador_max=10):
    if inicio > fim or inicio < 0 or multiplicador_max < 1:
        raise ValueError("Parâmetros inválidos para a tabuada")

    for multiplicador in range(1, multiplicador_max + 1):
        for numero in range(inicio, fim + 1):
            resultado = numero * multiplicador
            print(f"{numero:2d} x {multiplicador:2d} = {resultado:3d}", end="    ")
        print()


def main():
    try:
        imprimir_tabuada()
    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
