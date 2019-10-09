"""19- Faça um vetor de tamanho 50 preenchido com o seguinte valor: (i + 5 * i) % (i + 1),
sendo i a posição do elemento no vetor. Em seguida, imprima o vetor na tela."""

vetor = []

for n in range(50):
    valor = ((n + 5) * n) / (n + 1)
    vetor.append(valor)

print(vetor)
