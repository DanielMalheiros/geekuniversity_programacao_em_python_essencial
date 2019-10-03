"""16- Faça um programa que leia um número inteiro positivo ímpar N e imprima
todos os números ímpares de 1 até N em ordem decrescente."""

n = int(input("Digite um número inteiro, positivo e ímpar: "))

if n > 0:
    if n % 2 != 0:
        for x in range(n, 0, -1):
            if x % 2 != 0:
                print(x)
    else:
        print("Número inválido. ")
else:
    print("Número inválido. ")