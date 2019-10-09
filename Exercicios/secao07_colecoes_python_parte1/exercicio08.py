"""8- Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos
em ordem inversa."""

indice = 0
vetor = []

while indice < 6:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/6)"))
    vetor.append(valor)
    indice += 1

print(f"Lista: {vetor}\nLista invertida: {vetor[::-1]}")
