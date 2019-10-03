"""18- Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles
quantas vezes o maior número for lido. A quantidade de números a serem lidos deve ser
fornecida pelo usuário."""

qtd_num = int(input("Quantos números devem ser lidos? "))
maior = -99999999999

for _ in range(qtd_num):
    num = int(input("Informe um número: "))
    if num > maior:
        maior = num

print(f"O maior número informado é {maior}.")