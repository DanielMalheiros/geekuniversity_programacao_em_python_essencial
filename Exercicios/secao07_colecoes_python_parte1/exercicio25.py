"""25- Faça um programa que preencha um vetor de tamanho 100 com os 100 primeiros naturais que não
são multiplos de 7 ou que terminam com 7."""

numero = 1
contador = 0
vetor = []

while contador < 100:
    if numero % 7 != 0 and str(numero)[-1] != '7':
        vetor.append(numero)
        contador += 1
    numero += 1
print(vetor)
print(len(vetor))
