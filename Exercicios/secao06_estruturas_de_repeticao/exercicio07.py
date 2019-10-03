"""7- Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e
imprima sua média."""

soma = 0
valor_valido = 0

valor = int(input("Insira um valor: "))

while True:
    if valor > 0:
        soma = soma + valor
        valor_valido = valor_valido + 1
        if valor_valido == 10:
            break
        valor = int(input("Insira um valor: "))
    else:
        print("Valor inválido")
        valor = int(input("Insira um valor: "))

print(f"A média entre estes valores é {soma/10}")