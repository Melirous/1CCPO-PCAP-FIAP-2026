nomes = ["João", "Lucas", "Jair", "Luis"]

# for i in range(len(nomes)):
#     if i > 0:
#         print(nomes[0], nomes[i])
# for i in range(len(nomes)):
#     if i > 1:
#         print(nomes[1], nomes[i])
# for i in range(len(nomes)):
#     if i > 2:
#         print(nomes[2], nomes[i])

for i in range(len(nomes)):
    for j in range(i+1, len(nomes)):
        print(nomes[i], nomes[j])
