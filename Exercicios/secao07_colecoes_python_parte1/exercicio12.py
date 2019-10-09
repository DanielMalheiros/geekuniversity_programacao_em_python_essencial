"""12- Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
juntamente com o maior, o menor e a média dos valores."""

indice = 0
vetor = []

while indice < 5:
    valor = int(input(f"Digite um valor para o vetor ({indice+1}/5): "))
    vetor.append(valor)
    indice += 1

print(f"Vetor: {vetor}\nMaior valor: {max(vetor)}\nMenor valor: {min(vetor)}\nMédia dos valores:"
      f"{(sum(vetor) / 5):.2f}")
