"""17- Leia uma matriz 10 x 3 com as notas de 10 alunos em 3 provas. Em seguida, escreva o número de alunos cuja pior
nota foi na prova 1, o número de alunos cuja pior nota foi na prova 2, e o número de alunos cuja pior nota foi na prova
3. Em caso de empate das piores notas de um aluno, o criterio de desempate é arbitrário, mas o aluno deve ser
contabilizado apenas uma vez."""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
prova1 = 0
prova2 = 0
prova3 = 0

for i in range(10):
    for j in range(3):
        matriz[i][j] = int(input(f"ALUNO {i+1}:\nDigite nota da prova {j+1}: "))

for i in range(10):
    if min(matriz[i]) == matriz[i][0]:
        prova1 += 1
        if matriz[i][0] == matriz[i][1] or matriz[i][0] == matriz[i][2]:
            prova1 -= 1
    if min(matriz[i]) == matriz[i][1]:
        prova2 += 1
        if matriz[i][1] == matriz[i][2]:
            prova2 -= 1
    if min(matriz[i]) == matriz[i][2]:
        prova3 += 1


print(f"Número de alunos cuja pior nota foi na prova 1: {prova1}\nNúmero de alunos cuja pior nota foi na prova 2:"
      f"{prova2}\nNúmero de alunos cuja pior nota foi na prova 3: {prova3}")
