"""60- Faça um programa que leia vários números, calcule e mostre:
A soma dos números digitados
A quantidade de números digitados
A média dos números digitados
O maior número digitado
O menor número digitado
A média dos números pares

Finalize a entrada de dados quando o usuário digitar 0."""

num = int(input("Insira um número: "))
soma = 0
contador = 0
soma_par = 0
contador_par = 0
maior = -99999999
menor = 999999999


while num != 0:
    contador += 1
    soma += num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    if num % 2 == 0:
        soma_par += num
        contador_par += 1
    num = int(input("Insira um número: "))

print(f"A soma dos números é {soma}.\nA quantidade de numeros inseridos foi de {contador}.\n"
      f"A média é {soma / contador:.2f}.\nO menor número foi {menor}.\nO maior foi {maior}.\n"
      f"A média dos números pares é de {soma_par / contador_par:.2f}.")
