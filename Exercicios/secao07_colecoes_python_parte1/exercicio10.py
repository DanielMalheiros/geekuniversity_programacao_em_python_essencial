"""10- Faça um programa para ler a nota da prova de 15 alunos e armazene num vetor, valcule e
imprima a média geral."""

indice = 0
vetor = []

while indice < 15:
    nota = int(input(f"Insira a nota ({indice+1}/15): "))
    if 0 < nota < 11:
        vetor.append(nota)
        indice += 1
    else:
        print("Nota inválida.")

print(f"A média geral entre as quinze notas é de {(sum(vetor) / 15):.2f}.")
