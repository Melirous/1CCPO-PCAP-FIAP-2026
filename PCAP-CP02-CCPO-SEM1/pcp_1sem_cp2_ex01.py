origem = int(input("Digite o estado de origem(1 à 5):")) #
pesot = int(input("Digite o peso do caminhão em toneladas:"))
codigo = int(input("Digite o código da carga(10 à 40):"))

pesok = pesot * 1000

if codigo >= 10  <= 20:
    carga = pesok * 100
elif codigo >= 21 <= 30:
    carga = pesok * 250
else:
    carga = pesok * 340

if origem == 1:
    imposto = carga * 0.35
elif origem == 2:
    imposto = carga * 0.25
elif origem == 3:
    imposto = carga *0.15
elif origem == 4:
    imposto = carga * 0.05
else:
    imposto = carga * 1

total = carga + imposto

print(f"O peso da carga é de: {pesok} Kilos")
print(f"O valor da carga é de: R$ {carga:.2f}")
print(f"O valor do imposto é de: R$ {imposto:.2f}")
print(f"O valor total é de: R$ {total:.2f}")



