"""46- Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
Número lido: 123. Número gerado: 321."""

num = int(input("Insira um número de 3 dígitos."))
print(num[::-1])
