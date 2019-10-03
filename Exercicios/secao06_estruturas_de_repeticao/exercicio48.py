"""48- Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos valores
não ultrapassem quatro milhões."""

a = 0
b = 1
soma = 0

while(b < 4_000_000):
    c = a
    a = b
    b = a + c
    if b %  2 == 0:
        soma += b
print(soma)