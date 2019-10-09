"""22- Faça um programa que leia dois vetores de 10 posições e calcule outro vetor contendo, nas posições
pares os valores do primeiro e nas posições impares os valores do segundo."""

indice_a = 0
vetor_a = []
indice_b = 0
vetor_b = []
vetor_c = list(range(20))

while indice_a < 10:
    valor = int(input(f"Digite um número inteiro para o vetor A ({indice_a+1}/10): "))
    vetor_a.append(valor)
    indice_a += 1

while indice_b < 10:
    valor = int(input(f"Digite um número inteiro para o vetor B ({indice_b+1}/10): "))
    vetor_b.append(valor)
    indice_b += 1

vetor_c[0] = vetor_a[0]
vetor_c[1] = vetor_b[0]
vetor_c[2] = vetor_a[1]
vetor_c[3] = vetor_b[1]
vetor_c[4] = vetor_a[2]
vetor_c[5] = vetor_b[2]
vetor_c[6] = vetor_a[3]
vetor_c[7] = vetor_b[3]
vetor_c[8] = vetor_a[4]
vetor_c[9] = vetor_b[4]
vetor_c[10] = vetor_a[5]
vetor_c[11] = vetor_b[5]
vetor_c[12] = vetor_a[6]
vetor_c[13] = vetor_b[6]
vetor_c[14] = vetor_a[7]
vetor_c[15] = vetor_b[7]
vetor_c[16] = vetor_a[8]
vetor_c[17] = vetor_b[8]
vetor_c[18] = vetor_a[9]
vetor_c[19] = vetor_b[9]

print(vetor_c)
