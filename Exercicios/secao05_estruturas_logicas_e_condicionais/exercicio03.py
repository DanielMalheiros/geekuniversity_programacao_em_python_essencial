"""3- Leia um número real. Se o número for positivo imprima sua raiz quadrada:
Do contrario, imprima o número ao quadrado."""

num = float(input("Escolha um número real: "))

if num < 0:
    print(f"{num} ao quadrado é {num ** 2}.")
if num > 0:
    print(f"A raiz quadrada de {num} é {num ** (1/2):.2f}.")
