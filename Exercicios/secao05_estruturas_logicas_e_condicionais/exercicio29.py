"""29- Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros
menores que 100. Escolha números aleatórios entre 1 e 10 e mostre na tela a pergunta: faça a
soma de a + b, onde a e b são números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno
e mostre para eles as perguntas e as respostas corretas, além de quantas vezes o aluno acertou."""

r1 = int(input("Quanto é 10 + 10? "))
r2 = int(input("Quanto é 5 + 20? "))
r3 = int(input("Quanto é 1 + 6? "))
r4 = int(input("Quanto é 40 + 40? "))
r5 = int((input("Quanto é 1 + 1? ")))
acertos = 0

if r1 != 20:
    print("Errado: 10 + 10 = 20!")
elif r1 == 20:
    print("Certo: 10 + 10 = 20!")
    acertos = acertos + 1

if r2 != 25:
    print("Errado: 5 + 20 = 25!")
elif r2 == 25:
    print("Certo: 5 + 2- = 25!")
    acertos = acertos + 1

if r3 != 7:
    print("Errado: 1 + 6 = 7!")
elif r3 == 7:
    print("Certo: 1 + 6- = 7!")
    acertos = acertos + 1

if r4 != 80:
    print("Errado: 40 + 40 = 80!")
elif r4 == 80:
    print("Certo: 40 + 40- = 80!")
    acertos = acertos + 1

if r5 != 2:
    print("Errado: 1 + 1 = 2!")
elif r5 == 2:
    print("Certo: 1 + 1- = 2!")
    acertos = acertos + 1

print(f"Acertos: {acertos}")

