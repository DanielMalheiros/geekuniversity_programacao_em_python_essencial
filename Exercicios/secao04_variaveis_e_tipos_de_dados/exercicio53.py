"""53- Faça um programa para ler as dimensões de um terreno (comprimento c e largura l), bem como o
preço do metro de tela p. Imprima o custo para cercar este mesmo terreno com tela."""

c = float(input("Insira o comprimento do terreno: "))
l = float(input("Insira a largura o terreno: "))
p = float(input("Insira o preço do metro de tela em reais: "))
area = c * l
print(f"O valor total em telas será R${area * p}")
