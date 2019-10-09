#  Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

indice = 0
contador = 0
vetor = []

while indice < 10:
    valor = int(input(f"Digite um valor para o vetor: ({indice+1}/10)"))
    vetor.append(valor)
    indice += 1

for elemento in vetor:
    if elemento % 2 == 0:
        contador += 1

print(f"O vetor {vetor} possui {contador} elementos pares.")