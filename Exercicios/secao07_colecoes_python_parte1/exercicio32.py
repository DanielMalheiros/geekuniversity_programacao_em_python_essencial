"""32- Leia dois vetores de inteiros x e y, cada um com 5 elementos (assuma que o usuário não informa
elementos repetidos). Calcule e mostre os vetores resultantes em cada sado abaixo:
-Soma entre x e y: soma de cada elemento de x com o elemento da mesma posição em y.
-Produto entre x e y: multiplicação de cada elemento de x com o elemento da mesma posição em y.
-Diferença entre x e y: todos os elementos de x que não existam em y.
-Interseção entre x e y: apenas os elementos que aparecem nos dois vetores.
-União entre x e y: todos os elementos de x e todos os elementos de y que não estão em x."""

contador = 0
vetorx = []
vetory = []
soma = []
produto = []

while contador < 5:
    valor = int(input(f"Digite um valor para o primeiro vetor ({contador+1}/5): "))
    vetorx.append(valor)
    contador += 1

contador = 0

while contador < 5:
    valor = int(input(f"Digite um valor para o segundo vetor ({contador+1}/5): "))
    vetory.append(valor)
    contador += 1

setx = set(vetorx)
sety = set(vetory)

for buffer in range(5):
    valorsoma = vetorx[buffer] + vetory[buffer]
    soma.append(valorsoma)
    valorproduto = vetorx[buffer] * vetory[buffer]
    produto.append(valorproduto)

print(f"A soma entre os elementos de mesmo indice entre vetores X e Y: {soma}\nO produto entre os"
      f" elementos de mesmo indice entre os vetores X e Y: {produto}\nDiferença entre X e Y: {setx.difference(sety)}\n"
      f"Interseção entre X e Y: {setx.intersection(sety)}\nUnião entre X e Y: {setx.union(sety)}")
