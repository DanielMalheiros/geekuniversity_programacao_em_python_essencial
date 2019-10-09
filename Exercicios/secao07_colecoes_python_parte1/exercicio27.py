"""27- Leia 10 números inteiros e armazene em um vetor. Em seguida, escreva os elementos que são
primos e suas respectivas posições do vetor."""

contador = 0
vetor = {}
tot = 0

while contador < 10:
    valor = int(input(f"Insira um valor para o vetor ({contador+1}/10): "))
    vetor[contador] = valor
    contador += 1
print(vetor)

for chave in vetor:
    for n in range(1, vetor[chave]+1):
        if vetor[chave] % n == 0:
            tot += 1
    if tot == 2:
        print(f"{vetor[chave]} é um número primo e está na posição {chave} do vetor.")
    tot = 0
