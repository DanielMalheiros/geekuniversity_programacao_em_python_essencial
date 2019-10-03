"""13- Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares
de 0 até N em ordem crescente."""

n = int(input("Digite um número inteiro e positivo: "))

if n > 0:
    if n % 2 == 0:
        for x in range(n+1):
            if x % 2 == 0:
                print(x)
    else:
        print("Número inválido.")
else:
    print("Número inválido.")