"""35- Faça um programa que some os números impares contidos em um intervalo definido pelo usuário. O usuário define
o valor inicial do intervalo e o valor final deste intervalo e o programa deve somar todos os números ímpares
contidos neste intervalo. Caso o usuário digite um intervalo inválido (ex. o primeiro número maior que o segundo)
deve ser escrito uma mensagem de erro na tela, "Intervalo de valores inválido" eo programa termina."""

v1 = int(input("Digite o valor inicial: "))
v2 = int(input("Digite o valor final: "))
soma = 0

if v2 > v1:
    for n in range(v1 + 1, v2):
        if n % 2 != 0:
            soma += n
else:
    print("Intervalo de valores inválido.")

print(f"A soma dos ímpares neste intervalo de valores é {soma}.")