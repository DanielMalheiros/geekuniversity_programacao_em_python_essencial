"""15- Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão é:
G = R * pi/180, sendo G o ângulo em graus, R em radianos e pi = 3.14"""

r = float(input("Qual o ângulo de X em radianos? "))
print(f"Este ângulo equivale a {r * (180 / 3.14)} graus.")