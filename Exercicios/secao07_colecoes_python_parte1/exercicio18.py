"""18- Faça um programa que leia um vetor de 10 números. Leia um número X. Conte os
múltiplos de um número inteiro X no vetor e mostre-os na tela."""

indice = 0
vetor = []

while indice < 10:
    valor = int(input(f"Digite um número para o vetor ({indice+1}/10): "))
    vetor.append(valor)
    indice += 1

x = int(input("Insira um valor para X: "))

for elemento in vetor:
    if elemento % x == 0:
        print(f"O valor {elemento} é multiplo de {x}.")
