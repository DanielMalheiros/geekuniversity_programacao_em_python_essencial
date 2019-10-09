"""15- Leia uma matriz 5x10 que se refere a respostas de 10 questões de múltipla escolha, referentes
a 5 alunos. Leia também um vetor de 10 posições contendo o gabarito de respostas que podem ser a, b, c ou
d. Seu programa deverá comparar as respostas de cada candidato com o gabarito e emitir um vetor denominado
resultado, contendo a pontuação correspondente a cada aluno."""

matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
gabarito = ['a', 'a', 'b', 'c', 'd', 'd', 'a', 'b', 'c', 'b']
soma = 0
resultado = []

for i in range(5):
    for j in range(10):
        matriz[i][j] = input(f"(Aluno {i+1}) Qual a resposta da pergunta {j+1}?\n(a) (b) (c) (d):")

for i in range(5):
    for j in range(10):
        if matriz[i][j] == gabarito[j]:
            soma += 1
    print(f"O aluno {i+1} acertou {soma} questões.")
    resultado.append(soma)
    soma = 0

print(resultado)
