"""22- Leia a idade e o tempo de serviço de um trabalhador e escreva se ele
pode ou não se aposentar. As condições para aposentadoria são:

a) Ter pelo menos 65 anos.
b) Ou ter trabalhado por pelo menos 30 anos
c) Ou ter pelo menos 60 anos e trabalhado por pelo menos 25 anos"""

idade = int(input("Qual sua idade? "))
trab = int(input("Você já trabalhou quantos anos? "))

if idade >= 65:
    print("Está apto a se aposentar.")
elif idade >= 60 and trab >= 25:
    print("Está apto a se aposentar.")
elif trab >= 30:
    print("Está apto a se aposentar.")
else:
    print("Ainda não está apto a se aposentar.")
