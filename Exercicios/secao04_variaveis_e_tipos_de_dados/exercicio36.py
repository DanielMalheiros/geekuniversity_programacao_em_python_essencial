"""36- Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula: V = pi * raio ** 2 * altura,
onde pi = 3,141592."""

altura = float(input("Qual a altura do cilindro em centímetros? "))
raio = float(input("Qual é o raio do cilindro em centímetros? "))
area = 3.141592 * (raio ** 2) * altura
print(f"A área do cilindro será de {area:.2f} centímetros quadrados.")
