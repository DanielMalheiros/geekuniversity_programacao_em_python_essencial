"""20- Leia um valor de massa em quilogramas e apresente-o convertido em libras. A fórmula de
conversão é L = K / 0,45, sendo K a massa em quilogramas e L a massa em libras."""

m_quilo = float(input("Defina um valor de massa em quilogramas: "))
print(f"{m_quilo} em quilogramas equivale a {m_quilo / 0.45:.2f} libras.")