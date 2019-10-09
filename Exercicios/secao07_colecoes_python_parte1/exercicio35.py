"""35- Faça um programa que leia dois números a e b (positivos menores que 10000) e:
-Crie um vetor onde cada posição é um algarismo do número. A primeira posição é o algarismo
menos significativo;
-Crie um vetor que seja a soma de a e b, mas faça-o usando apenas os vetores construidos anteriormente."""

a = int(input("Digite um valor A: "))
b = int(input("Digite um valor B: "))

vetor_a = list(str(a))
vetor_b = list(str(b))
vetor_aint = [int(i) for i in vetor_a]
vetor_bint = [int(i) for i in vetor_b]

print(vetor_aint)
print(vetor_bint)
