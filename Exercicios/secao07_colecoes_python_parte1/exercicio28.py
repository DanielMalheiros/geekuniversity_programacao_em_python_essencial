"""2- Leia 10 números inteiros e armazene em um vetor V. Crie dois novos vetores v1 e v22. Copie os
valores ímpares de v para v1, e os valores pares de v para v2. Note que cada um dos vetores v1 e v2 têm
no maximo, 10 elemenetos, mas nem todos os elementos são utilizados. No final, escreva os elementos utilizados
de v1 e v2."""

contador = 0
v = []
v1 = []
v2 = []

while contador < 10:
    valor = int(input(f"Digite um valor para o vetor V ({contador+1}/10): "))
    v.append(valor)
    contador += 1

for elemento in v:
    if elemento % 2 == 0:
        v1.append(elemento)
    else:
        v2.append(elemento)

print(f"Lista com pares: {v1}")
print(f"Lista com ímpares {v2}")
