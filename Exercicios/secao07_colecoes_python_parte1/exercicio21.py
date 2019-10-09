"""21- Faça um programa que receba do usuário dois vetores, A e B, com 10 números inteiros cada. Crie um
novo vetor denominado C calculando C = A - B. Mostre na tela os dados do vetor C."""

indice_a = 0
vetor_a = []
indice_b = 0
vetor_b = []
vetor_c = list(range(10))

while indice_a < 10:
    valor = int(input(f"Digite um número inteiro para o vetor A ({indice_a+1}/10): "))
    vetor_a.append(valor)
    indice_a += 1

while indice_b < 10:
    valor = int(input(f"Digite um número inteiro para o vetor B ({indice_b+1}/10): "))
    vetor_b.append(valor)
    indice_b += 1

for index in range(10):
    vetor_c[index] = vetor_a[index] - vetor_b[index]

print(vetor_c)
