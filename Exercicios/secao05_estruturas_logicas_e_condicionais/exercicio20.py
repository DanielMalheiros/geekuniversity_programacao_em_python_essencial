"""20- Dados três valores, A,B,C, verificar se eles podem ser valores dos lados de um triângulo e,
se forem, se é um trinâgulo escaleno, equilátero ou isóscele, considerando
os seguintes conceitos:
a) O comprimento de cada lado de um triângulo é menor do que a soma
dos outros dois lados.
b) Chama-se equilátero o triângulo que tem três lados iguais.
c) Recebe o nome de escaleno o triângulo que tem os três lados diferentes."""

a = float(input("Defina um dos lados do triângulo: "))
b = float(input("Defina mais um lado do triângulo: "))
c = float(input("Defina o ultimo lado do triãngulo: "))

if a < b + c and b < a + c and c < b + a:
    if a == b and b == c:
        print("Trata-se de um triângulo EQUILÁTERO.")
    elif a != b and b != c:
        print("Trata-se de um triângulo ESCALENO.")
    else:
        print("Trata-se de um triângulo ISÓSCELE.")
else:
    print("Valores para triângulo inválidos.")
