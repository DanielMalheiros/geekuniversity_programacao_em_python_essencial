"""15- Leia um vetor com 20 números inteiros. Escreva os elementos do vetor eliminando elementos
repetidos."""

indice = 0
vetor = []

while indice < 20:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/20): "))
    vetor.append(valor)
    indice += 1
    if vetor.count(valor) > 1:
        vetor.remove(valor)
print(vetor)
