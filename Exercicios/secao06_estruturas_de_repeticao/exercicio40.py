"""40- Elabore um programa que gaça leitura de vários números inteiros, até que se digite um número negativo.
O programa tem que tetornar o maior e o menor número lido."""

num = int(input("Digite um número inteiro: "))
maior = 0
menor = 99999

while num >= 0:
    if num > maior:
        maior = num

    if num < menor:
        menor = num

    num = int(input("Digite um número inteiro: "))

print(f"O maior valor inserido foi {maior} e o menor foi {menor}.")
