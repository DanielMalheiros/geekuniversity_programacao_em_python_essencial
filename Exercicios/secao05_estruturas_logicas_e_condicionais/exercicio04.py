"""4- Faça um programa que leia um número e, caso ele seja positivo, calcule
e mostre:
a) O número digitado ao quadrado.
b)A raiz quadrada do número digitado."""

num = int(input("Escolha um número: "))

if num > 0:
    print(f"{num} ao quadrado é {num ** 2}")
    print(f"A raiz quadrada de {num} é {num ** (1/2):.2f}.")
