def calcular_operacao(a, op, c):
    try:
        if op == "+":
            return a + c
        elif op == "-":
            return a - c
        elif op == "*":
            return a * c
        elif op == "/":
            if c == 0:
                return 0
            return a / c
        else:
            return 0
    except (TypeError, ZeroDivisionError):
        return 0


A = [7, 4, 9, 3, 6]
B = ["+", "-", "/", "*", "/"]
C = [1, 3, 3, 2, 0]

D = []
for i in range(len(A)):
    resultado = calcular_operacao(A[i], B[i], C[i])
    D.append(int(resultado))

print("Vetor D:", D)

assert D == [
    8,
    1,
    3,
    6,
    0,
], f"Erro: resultado {D} diferente do esperado [8, 1, 3, 6, 0]"

print("Todos os resultados estão corretos!")
