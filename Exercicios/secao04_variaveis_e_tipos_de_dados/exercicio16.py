"""16- Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é C = P * 2,54, sendo C o comprimento em centímetros e P o
comprimento em polegadas."""

polegadas = float(input("Qual o comprimento em polegadas? "))
print(f"Este comprimento equivale a {polegadas * 2.54:.2f} centímetros.")