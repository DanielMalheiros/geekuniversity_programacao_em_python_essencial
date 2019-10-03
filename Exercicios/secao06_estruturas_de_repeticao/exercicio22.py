"""22- Escreva um programa completo que permita a qualquer aluno introduzir, via teclado, uma sequencia
arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a média
aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa,
o qua terminará quando for introduzido um valor que não seja válido como nota de aprovação."""

nota = int(input("Insira uma nota de 10 a 20: "))
media = 0
qtd = 0  # quantidade de valores inseridos

while nota >= 10 and nota <= 20:
    media = media + nota
    qtd = qtd + 1
    nota = int(input("Insira uma nota de 10 a 20: "))

print(f"A média aritmética entre os valores inseridos é {media / qtd}.")