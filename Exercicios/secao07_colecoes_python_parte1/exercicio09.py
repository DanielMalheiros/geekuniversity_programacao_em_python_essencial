"""9- Crie um programa que lê 6 valores inteiros pares e, em seguida, mostre na tela os valores
lidos na ordem inversa."""

indice = 0
vetor = []

while indice < 10:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/10)"))
    if valor % 2 == 0:
        vetor.append(valor)
        indice += 1
    else:
        print("Valor inválido!")

print(f"Lista de números pares: {vetor}\nLista invertida: {vetor[::-1]}")
