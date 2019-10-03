"""19- Faça um programa para verificar se determinado número inteiro é divisível
por 3 ou 5 mas não simultaneamente pelos 2."""

num = int(input("Escolha um número: "))

if num % 3 == 0 or num % 5 == 0:
    if num % 3 == 0 and num % 5 != 0:
        print(f"O número {num} é divisível por 3, mas não por 5.")
    elif num % 5 == 0 and num % 3 != 0:
        print(f"O número {num} é divisível por 5, mas não por 3.")
    elif num % 5 == 0 and num % 3 == 0:
        print(f"O número {num} é divisível por 3 e 5.")
else:
    print(f"O número {num} não é divisível nem por 3 e nem por 5")
