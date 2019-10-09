#  2- Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

indice = 0
lista = []

while indice < 6:
    valor = int(input(f"Digite um valor inteiro ({indice+1}/6): "))
    lista.append(valor)
    indice += 1

print(lista)
