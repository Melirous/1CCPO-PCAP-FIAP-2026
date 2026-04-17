cp1 = float(input("Insira o valor da nota do Checkpoint 1:")) #
cp2 = float(input("Insira o valor da nota do Checkpoint 2:"))
cp3 = float(input("Insira o valor da nota do Checkpoint 3:"))
sp1 = float(input("Insira o valor da nota do Sprint 1:"))
sp2 = float(input("Insira o valor da nota da Sprint 2:"))
gs = float(input("Insira o valor da nota do Global Solutions:"))

menor = cp1

if cp2 < menor:
    menor = cp2

if cp3 < menor:
    menor = cp3

somacp = cp1 + cp2 + cp3 - menor

parcial = (somacp + sp1 + sp2) / 4

media = parcial * 0.4 + gs * 0.6

peso = media * 0.4

print(f"Média do semestre: {media:.1f}")
print(f"Média com peso: {peso:.1f}")