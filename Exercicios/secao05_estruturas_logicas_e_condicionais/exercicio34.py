"""34- Leia a nota e o número de faltas de um aluno e escreva seu conceito.
De acordo com a tabela abaixo, quando o aluno tem mais de 20 faltas ocorre
uma redução de conceito.
NOTA           CONCEITO(ATÉ 20 FALTAS)       CONCEITO(MAIS DE 20 FALTAS)
9.0 até 10.0            A                               B
7.5 até 8.9             B                               C
5.0 até 7.4             C                               D
4.0 até 4.9             D                               E
0.0 até 3.9             E                               E
"""

nota = float(input("Insira sua nota: "))
falta = int(input("Insira a quantidade de faltas: "))

if nota > 10 or nota < 0:
    print("Nota inválida.")
elif nota >= 9.0:
    if falta <= 20:
        print("Conceito A")
    else:
        print("Conceito B")
elif nota >= 7.5 and nota < 9.0:
    if falta <= 20:
        print("Conceito B")
    else:
        print("Conceito C")
elif nota >= 5 and nota < 7.5:
    if falta <= 20:
        print("Conceito C")
    else:
        print("Conceito D")
elif nota >= 4.0 and nota < 5.0:
    if falta <= 20:
        print("Conceito D")
    else:
        print("Conceito E")
elif nota < 4.0:
    print("Conceito E")
