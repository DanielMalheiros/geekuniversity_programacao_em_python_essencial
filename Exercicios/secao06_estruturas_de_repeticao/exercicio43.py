"""43- Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for
informada a idade 0) e calcule a idade média desse grupo."""

idade = int(input("Insira uma idade:"))
soma = 0
contador = 0

while idade != 0:
    if idade < 0:
        print("Idade inválida")
        idade = int(input("Insira uma idade: "))
    soma += idade
    contador += 1
    idade = int(input("Insira uma idade: "))


print(f"A media entre as idades será {soma / contador}.")

