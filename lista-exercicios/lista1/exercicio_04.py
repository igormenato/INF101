def multiplicar(x, y):
  return x * y

def main():
  x = float(input("Digite o valor de x: "))
  y = float(input("Digite o valor de y: "))
  result = multiplicar(x, y)
  print(f"O resultado de {x} multiplicado por {y} é {result}")

if __name__ == "__main__":
  main()