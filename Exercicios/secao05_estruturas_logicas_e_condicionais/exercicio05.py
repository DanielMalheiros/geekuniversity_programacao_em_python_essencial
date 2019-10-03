"""5- Faça um programa que receba um número inteiro e verifique se este número
é par ou impar."""

num = int(input("Escolha um número: "))

if num % 2 == 0:
    print(f"O número {num} é par.")
else:
    print(f"O número {num} é impar.")