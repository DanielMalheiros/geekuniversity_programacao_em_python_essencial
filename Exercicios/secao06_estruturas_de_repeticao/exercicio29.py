"""29- Escreva um programa para calcular o valor da série, para 5 termos.
S = 0 + 1/2! + 2/4! + 3/6! +..."""

s = 0
# 0 + 1/2! + 2/4! + 3/6! + 4/8 + 5/10!
# 0 + 1/2! + 1/2! + 1/3! + 1/4! + 1/5!

for n in range(1, 6):
    cont = n
    f = 1
    while cont > 0:     # 1/1 + 1/2 + 1/6 + 1/24 + 1/120
        f *= cont
        cont -= 1
    s += 1 / f

print(s - 1/2)
