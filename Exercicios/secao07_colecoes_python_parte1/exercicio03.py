"""3- Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos componentes
desse vetor, armazenando o resultado em outro vetor. Os conjuntos têm 10 elementos cada. Imprima
todos os conjuntos."""

listareal = []
listaaoquadrado = []
indice = 0

while indice < 10:
    real = float(input(f"Digite um número real ({indice+1}/10): "))
    listareal.append(real)
    indice += 1

for elemento in listareal:
    elementoaoquadrado = elemento ** 2
    listaaoquadrado.append(elementoaoquadrado)

print(f"Lista: {listareal}.")
print(f"Lista elevada ao quadrado: {listaaoquadrado}.")
