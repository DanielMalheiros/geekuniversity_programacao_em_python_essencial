"""42- Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos
valores lidos: o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero."""

num = int(input("Insira um número: "))

while num > 0:
    print(f"Ao quadrado: {num ** 2}")
    print(f"Ao cubo: {num ** 3}")
    print(f"Raiz quadrada: {num ** 1/2}")
    num = int(input("Insira um número: "))
