"""19- Faça um programa que leia uma matriz de 5 linhas e 4 colunas contendo as seguintes informações sobre os alunos de
uma disciplina, sendo todas as informações do tipo inteiro:
- Primeira coluna: número de matrícula
- Segunda coluna: média das provas
- Terceiro coluna: média dos trabalhos
- Quarta coluna: nota final

Elabore um programa que:
a)Leia as três primeiras informações de cada aluno
b)Calcule a nota final como sendo a soma da média das provas e da média dos trabalhos
c)Imprima a matrícula do aluno que obteve a maior nota final (assuma que só existe uma maior nota)
d)Imprima a média aritmética das notas finais"""

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
modalidade = 0
soma = 0
mediaaritmetica = 0

for i in range(5):
    matriz[i][0] = int(input(f"ALUNO {i+1}\nInforme seu número de matrícula:"))
for i in range(5):
    matriz[i][1] = int(input(f"ALUNO {i+1}\nInforme a média de suas provas:"))
for i in range(5):
    matriz[i][2] = int(input(f"ALUNO {i + 1}\nInforme a média de seus trabalhos:"))
for i in range(5):
    matriz[i][3] = matriz[i][1] + matriz[i][2]


for i in range(5):
    for j in range(4):
        if j == 0:
            modalidade = 'MATRICULA'
        if j == 1:
            modalidade = 'MÉDIA PROVAS'
        if j == 2:
            modalidade = 'MÉDIA TRABALHOS'
        if j == 3:
            modalidade = 'NOTA FINAL'
        print(f"ALUNO {i+1} - {modalidade}:  [{matriz[i][j]:^3}] ", end=' ')
    print( )

for i in range(5):
    soma += matriz[i][3]
    mediaaritmetica = soma / 5

print(f"\nMédia Aritmética: {mediaaritmetica}")
