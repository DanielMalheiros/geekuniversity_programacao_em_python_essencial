"""27- Em matemática, o número harmônico designado por H(n) define-se como sendo a soma
da série harmónica:
H(n) = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n)."""

n = int(input("Insira um valor N inteiro e positivo: "))
h = 0
hn = 0

if n > 0:
    for x in range(1, n+1):
        h = 1 / x
        hn = hn + h
else:
    print("Número invalido.")

print(f"O número harmônico de {n} é {hn:.2f}.")