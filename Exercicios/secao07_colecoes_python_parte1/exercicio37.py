"""37- Considere um vetor A, com 11 elementos onde A1 < A2 <...< A6 > A7 > A8 >...> A11, ou seja
está ordenano em ordem crescente até o sexto elemento, e, a partir desse elemento está ordenado em
ordem decrescente. Dado o vetor, proponha um algoritmo para ordenar os elementos"""

contador = 0
vetor = []
vetorordenado = []

while contador < 11:
    valor = int(input(f"Digite um valor para o vetor ({contador+1}/11)"))
    vetor.append(valor)
    contador += 1

vetor.sort()
vetorordenado = vetor[5:11] + vetor[0:5][::-1]
print(vetorordenado)
