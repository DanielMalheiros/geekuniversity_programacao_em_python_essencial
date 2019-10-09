"""26- Faça um programa que receba 6 números inteiros e mostre:
-Os números pares digitados;
-A soma dos números pares digitados;
-Os números ímpares digitados;
-A quantidade de números ímpares digitados;
"""

contador = 0
v = []
v1 = []
v2 = []

while contador < 6:
    valor = int(input(f"Digite um valor para o vetor V ({contador+1}/10): "))
    v.append(valor)
    contador += 1

for elemento in v:
    if elemento % 2 == 0:
        v1.append(elemento)
    else:
        v2.append(elemento)

print(f"Números pares: {v1}\nSoma de números pares digitados: {sum(v1)}\nNúmeros ímpares: {v2}\n"
      f"Quantidade de números ímpares: {len(v2)}")
