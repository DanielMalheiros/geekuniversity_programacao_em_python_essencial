"""Faça um programa que leia um vetor de 5 posições para números reais e, depois, um código inteiro.
Se o código for zero, finalize o programa; se for 1, mostre o vetor na ordem direta; se for 2, mostre
o vetor na ordem inversa. Caso o código for diferente de 1 e 2, escreva uma mensagem informando que o
código é inválido."""

indice = 0
vetor = []

while indice < 5:
    valor = float(input(f"Digite um valor real para o vetor ({indice+1}/5): "))
    vetor.append(valor)
    indice += 1

codigo = int(input("Digite um código:\n1- Imprimir vetor em ordem direta.\n2- Imprimir vetor em ordem inversa"
                   "\n0- Finalizar programa"))

while codigo != 0:
    if codigo == 1:
        print(vetor)
        break
    elif codigo == 2:
        print(vetor[::-1])
        break
    elif codigo != 1 and codigo != 2 and codigo != 0:
        print("Codigo inválido!")
        codigo = int(input("Digite um código: "))
