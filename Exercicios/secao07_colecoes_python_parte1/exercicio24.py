"""24- Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número
do aluno e o segundo representando sua altura em metros. Encontre o aluno mais baixo e o aluno mais
alto. Mostre o número do aluno mais baixo e do aluno mais alto, juntamente com suas alturas."""

alunos = {}
maisalto = 0

for n in range(10):
    altura = float(input(f"Digite a altura do aluno {n+1}: "))
    alunos[n+1] = altura
print(alunos)

for i, j in alunos.items():
    if j == max(alunos.values()):
        print(f"O aluno mais alto é o de número {i}, medindo {j}")
    if j == min(alunos.values()):
        print(f"O aluno mais alto é o de número {i}, medindo {j}")
