"""38- Peça ao usuário para digitar dez valores numéricos e ordene por ordem crescente esses valores,
guardando-os num vetor. Ordene o valor assim que ele for digitado. Mostre ao final na tela os valores
em ordem."""

contador = 0
vetor = [10]

while contador < 10:
    valor = int(input(f"Digite um valor para o vetor ({contador+1}/10): "))
    vetor.append(valor)
    vetor.sort()
    contador += 1

print(vetor)
