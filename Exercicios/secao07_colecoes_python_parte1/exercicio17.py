"""17- Leia um vetor de 10 posições e atribua valor 0 para todos os elementos que possuírem
valores negativos."""

indice = 0
vetor = []

while indice < 10:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/10): "))
    vetor.append(valor)
    indice += 1

for elemento in vetor:
    if elemento < 0:
        vetor[vetor.index(elemento)] = 0

print(vetor)
