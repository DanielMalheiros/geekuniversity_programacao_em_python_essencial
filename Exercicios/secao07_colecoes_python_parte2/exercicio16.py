"""16- Faça um programa para corrigir uma prova com 10 questões de múltipla escolha (a, b, c, d ou e), em uma
turma com 3 alunos. Cada questão vale 1 ponto. Leia o gabarito, e para cada aluno leia sua matricula (numero inteiro) e
suas respostas. Calcule e escreva: Para cada aluno, escreva sua matrícula, suas respostas e sua nota. O percentual de
aprovação, assumindo média 7.0"""

matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
gabarito = ['a', 'b', 'c', 'c', 'e', 'd', 'e', 'a', 'b', 'b']
matricula = [0, 0, 0]
soma = 0
aprovado = 0

for i in range(3):
    matricula[i] = int(input(f"Aluno {i+1}, qual seu número de matricula?"))
    for j in range(10):
        matriz[i][j] = input(f"Aluno {i+1}, qual a resposta da pergunta {j+1}?\n(a) (b) (c) (d) (e): ")

for i in range(3):
    for j in range(10):
        if matriz[i][j] == gabarito[j]:
            soma += 1
            if soma >= 7:
                aprovado += 1
    print('--------------------------------------')
    print(f"Aluno: {i+1}\nMatricula: {matricula[i]}\nNota: {soma}\nRespostas: {matriz[i]}")
    soma = 0

print(f"--------------------------------------\nPercentual de aprovação: {aprovado / 3 * 100}%")
