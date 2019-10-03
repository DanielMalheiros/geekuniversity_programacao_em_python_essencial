"""33- Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente
os n primeiro naturais que são múltiplos de i ou de j e ou de ambos. Exemplo: para n = 6, i = 2
e j = 3 a saída deverá ser: 0,2,3,4,6,8.

n = int(input("Digite um número inteiro e positivo para N: "))
i = int(input("Digite um número inteiro e positivo para I: "))
j = int(input("Digite um número inteiro e positivo para J: "))"""

num = 0
cont = 0

while cont < n:
    if num % i == 0 or num % j == 0 or num % i == 0 and num % j == 0:
        print(num)
        num +=1
        cont += 1
    else:
        num += 1