"""17- Faça um programa que leia um número inteiro positivo N e calcule a soma dos
N primeiros números naturais."""

n = int(input("Digite um número inteiro e positivo: "))
soma = 0
if n > 0:
    for x in range(n+1):
        soma = soma + x
else:
    print("Número inválido.")

print(soma)