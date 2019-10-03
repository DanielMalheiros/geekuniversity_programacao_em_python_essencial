"""11- Escreva um programa que leia um número inteiro maior do que zero e devolva,
 na tela, a soma de todos os seus algarismos. Por exemplo, o número 251 corresponderá
 ao valor 8 (2 + 5 + 1). Se o número lido não for maior que zero, o programa deverá
 terminar com a mensagem "Número inválido"."""

num = int(input("Defina um valor inteiro maior que zero: "))
soma = 0

for x in str(num):
    soma += int(x)

print(soma)

