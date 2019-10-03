"""7- Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. A
fórmula de conversão é C = 5.0 * (F -32) / 9.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius."""

f = float(input("Defina uma temperatura em Fahrenheit: "))
print(f"{f} graus Fahrenheit equivalem a {5.0 * (f -32) / 9.0} graus Celsius.")
