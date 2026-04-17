nome = input("Nome do cliente: ") #
idade = int(input("Idade: "))
renda = float(input("Renda mensal: "))
valor = float(input("Valor do empréstimo: "))
parcelas = int(input("Número de parcelas (3 a 24): "))

def pode_aprovar(idade, renda, valor):
    if idade > 18 and valor <= renda * 20:
        return True
    return False

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    i = taxa
    n = parcelas
    pmt = valor * (i * (1 + i)**n) / ((1 + i)**n - 1)
    return pmt

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

if not pode_aprovar(idade, renda, valor):
    print(f"Empréstimo negado")
else:
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)

    print(f"Empréstimo aprovado")
    print(f"O cliente se chama: {nome}")
    print(f"O valor financiado é de: R$ {valor:.2f}")
    print(f"A taxa de juros é de: {taxa*100:.1f}% ao mês")
    print(f"O valor da parcela é de: R$ {parcela:.2f}")
    print(f"O total pago é de: R$ {total:.2f}")
    print(f"O total de juros: R$ {juros:.2f}")