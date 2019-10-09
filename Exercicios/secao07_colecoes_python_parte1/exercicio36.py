"""36- Leia um vetor com 10 números reais, ordene os elementos deste vetor, e, no final escreva
os elementos do vetor ordenado."""

contador = 0
vetor = []

while contador < 10:
    valor = float(input(f"Digite um número real para o vetor ({contador+1}/10): "))
    vetor.append(valor)
    contador += 1

vetor.sort()
print(vetor)
