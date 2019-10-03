"""25- Calcule as raizes da equação de segundo grau, lembrando que:
x = (-b + ou - lambda ** 1/2) / 2a e lambda = b ** 2 - 4 a * c
A varíavel a tem que ser diferente de zero. Caso contrario, imprima a mensagem: "Não é equação se segundo grau.
Se lambda < 0, imprima a mensagem "Não existe raiz". Se lambda = 0, existe uma raiz real. Imprima a raiz e a mensagem
"Raiz única. Se lambda > 0, imprima as duas raízes reais."""

a = float(input("Defina A:"))
b = float(input("Defina B:"))
c = float(input("Defina C:"))

delta = b ** 2 - (4 * a * c)
raiz1 = (-b + (delta ** 1/2)) / 2 * a
raiz2 = (-b - (delta ** 1/2)) / 2 * a

if a == 0:
    print("Não é uma equação de segundo grau.")
else:
    if delta < 0:
        print("Não existe raiz.")
    elif delta == 0:
        print("Existe uma raiz real:")
        print(f"{raiz1}")
    elif delta > 0:
        print("Existem duas raizes reais:")
        print(f"{raiz1} e {raiz2}")
