"""14- A nota final de um estudante é calculada a partir de três notas atribuídas
entre o intervalo de até 10, respectivamente a um trabalho de laboratório, a
uma avaliação semestral e a um exame final. A média das três notas mencionadas
anteriormente obedece aos pesos: Trabalho de laboratório: 2; Avaliação Semestral: 3;
Exame final: 5; De acordo com o resultado, mostre na tela se o aluno está reprovado
(média final entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça
todas as verificações necessarias."""

nota_lab = float(input("Insira a nota do trabalho de laboratório (0 a 10): "))
nota_as = float(input("Insira a nota da avaliação semestral (0 a 10): "))
nota_ef = float(input("Insira a nota do exame final (0 a 10): "))

if nota_lab < 0 or nota_lab > 10:
    print("Nota do trabalho de laboratório inválida.")
elif nota_as < 0 or nota_ef > 10:
    print("Nota da avaliação semestral inválida.")
elif nota_ef < 0 or nota_ef > 10:
    print("Nota do exame final inválida.")

media = ((nota_lab * 2) + (nota_as * 3) + (nota_ef * 5)) / 10
if media < 3:
    print(f"Aluno reprovado (Média {media:.2f})).")
elif media >= 3 and media < 5:
    print(f"Aluno de recuperação (Média {media:.2f}).")
else:
    print(f"Aluno aprovado! (Média {media:.2f})")
