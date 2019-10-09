"""20- Escreva um programa que leia números inteiros no intervalo [0, 50] e os armazene
em um vetor com 10 posições. Preencha um segundo vetor apenas com os números ímpares do
primeiro vetor. Imprima os dois vetores, 2 elementos por linha."""

indice = 0
vetor = []
vetorimpar = []

while indice < 10:
    valor = int(input(f"Digite um valor dentro do intervalo de [0, 50] para o vetor ({indice+1}/10): "))
    vetor.append(valor)
    if valor % 2 != 0:
        vetorimpar.append(valor)
    indice += 1

for elemento in range(len(vetorimpar)):
    print(vetor[elemento], vetorimpar[elemento])
