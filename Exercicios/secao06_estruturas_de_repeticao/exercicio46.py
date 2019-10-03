"""46- Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual
o número foi gerado, a cada tentativa o programa deverá informar se o chute é menor ou maior que o
número gerado. O programa acaba quando o usuário acerta o número gerado. O programa deve informar
em quantas tentativas o número foi descoberto."""

from random import randrange
count = 1
numero = randrange(1000)
escolha = int(input('Escolhi um número de 1 a 1000, tente adivinhar!'))
while escolha != numero:
    if escolha < numero:
        escolha = int(input('Tá baixo! =>'))
        count += 1
    if escolha > numero:
        escolha = int(input('Tá alto! =>'))
        count += 1
print(f'VOCÊ ACERTOU!!!\nForam {count} tentativas!')