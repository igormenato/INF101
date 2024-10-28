def imprimir_tabuada(inicio=1, fim=5, multiplicador_max=10):
    """
    Imprime a tabuada dos números no intervalo especificado.

    Args:
        inicio (int): Número inicial da tabuada (default: 1)
        fim (int): Número final da tabuada (default: 5)
        multiplicador_max (int): Valor máximo do multiplicador (default: 10)

    Raises:
        ValueError: Se os parâmetros não forem válidos
    """
    if inicio > fim or inicio < 0 or multiplicador_max < 1:
        raise ValueError("Parâmetros inválidos para a tabuada")

    for multiplicador in range(1, multiplicador_max + 1):
        for numero in range(inicio, fim + 1):
            resultado = numero * multiplicador
            # Usa formatação fixa para alinhar as colunas
            print(f"{numero:2d} x {multiplicador:2d} = {resultado:3d}", end="    ")
        print()


def main():
    try:
        imprimir_tabuada()
    except ValueError as e:
        print(f"Erro: {e}")


if __name__ == "__main__":
    main()
