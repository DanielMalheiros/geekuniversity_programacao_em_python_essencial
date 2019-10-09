"""11- Faça um programa que preencha um vetor com 10 números reais, calcule e mostre a quantidade
de números negativos e a soma dos números positivos desse vetor."""

indice = 0
contador = 0
soma = 0
vetor = []

while indice < 10:
    valor = float(input(f"Digite um número real para o vetor ({indice+1}/10): "))
    vetor.append(valor)
    indice += 1
    if valor < 0:
        contador += 1
    if valor > 0:
        soma += valor

print(f"No vetor {vetor} existem {contador} números negativos e a soma entre seus valores positivos"
      f"é de {soma}.")
