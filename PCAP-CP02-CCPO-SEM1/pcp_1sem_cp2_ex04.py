nome = input("Nome do funcionário: ") #
cargo = int(input("Cargo (1-4)(1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Salário base: "))
horas_extras = float(input("Horas extras trabalhadas: "))
faltas = int(input("Faltas no mês: "))
recebeu_bonus = input("Recebeu bônus? (sim ou não): ")

def calcular_horas_extras(salario_base, horas):
    valor_hora_extra = salario_base * 0.015
    return valor_hora_extra * horas

def calcular_descontos_faltas(salario_base, faltas):
    desconto_por_falta = salario_base * 0.02
    return desconto_por_falta * faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == 'sim':
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0

valor_horas_extras = calcular_horas_extras(salario_base, horas_extras)
valor_descontos = calcular_descontos_faltas(salario_base, faltas)
valor_bonus = calcular_bonus(cargo, recebeu_bonus)

total_acrescimos = valor_horas_extras + valor_bonus
salario_bruto = salario_base + total_acrescimos
salario_final = salario_bruto - valor_descontos

print(f"O funcionário se chama: {nome}")
print(f"O salário bruto é: R$ {salario_bruto:.2f}")
print(f"O total de acréscimos é: R$ {total_acrescimos:.2f}")
print(f"O total de descontos é: R$ {valor_descontos:.2f}")
print(f"O salário final é: R$ {salario_final:.2f}")