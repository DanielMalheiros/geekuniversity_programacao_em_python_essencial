"""7- Faça um programa que receba dois números e mostre o maior. Se por acaso
 os dois números forem iguais, imprima a mensagem "Números iguais". """

num1 = int(input("Escolha um valor: "))
num2 = int(input("Escolha mais um valor: "))

if num1 > num2:
    print(f"Maior valor: {num1}.")
elif num1 < num2:
    print(f"Maior valor: {num2}.")
else:
    print("Os valores são iguais.")
