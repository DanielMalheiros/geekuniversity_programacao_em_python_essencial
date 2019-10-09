"""14- Faça um programa que leia um vetor de 10 posições e verifique se existem valores
iguais e os escreva na tela."""

indice = 0
vetor = []

while indice < 10:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/10): "))
    vetor.append(valor)
    indice += 1

for elemento in vetor:
    contador = vetor.count(elemento)
    if contador >= 2:
        print(f"Existem um ou mais valores iguais à {elemento}.")
