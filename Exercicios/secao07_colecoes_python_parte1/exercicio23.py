"""23- Ler dois conjuntos de números reais, armazenando-os e vetores e calcular o produto escalar entre
eles. Os conjuntos têm 5 elementos cada. Imprimir os dois conjuntos e o produto escalar, sendo que o produto
escalar é dado por: x1 * y1 + x2 * y2 +...+...xn * yn."""

indice_a = 0
vetor_a = []
indice_b = 0
vetor_b = []
vetor_c = list(range(5))

while indice_a < 5:
    valor = float(input(f"Digite um número inteiro para o vetor A ({indice_a+1}/5): "))
    vetor_a.append(valor)
    indice_a += 1

while indice_b < 5:
    valor = float(input(f"Digite um número inteiro para o vetor B ({indice_b+1}/5): "))
    vetor_b.append(valor)
    indice_b += 1

for n in range(5):
    vetor_c[n] = (vetor_a[n] * vetor_b[n])
    print(vetor_c)

print(sum(vetor_c))
