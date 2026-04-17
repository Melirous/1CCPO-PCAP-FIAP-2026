A = int(input("Insira o valor do lado A do triângulo:")) #
B = int(input("Insira o valor do lado B do triângulo:"))
C = int(input("Insira o valor do lado C do triângulo:"))

if A >= B + C:
    print("Não forma Triângulo")
else:
    if A ** 2 == B ** 2 + C ** 2:
        print("Triângulo Retângulo")
    elif A ** 2 > B ** 2 + C ** 2:
        print("Triângulo Obtusângulo")
    else:
        print("Triângulo Acutângulo")

    if A == B == C:
        print("Triângulo Equilátero")
    elif A == B or B == C or A == C:
        print("Triângulo Isóceles")