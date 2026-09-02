# 1. Entrada de dados do usuário
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input(f"Digite a potência do {aparelho} em Watts (W): "))
horas_dia = float(input(f"Digite o tempo médio de uso diário do {aparelho} em horas: "))

# 2. Configurações de cálculo (tarifa fixa de energia)
VALOR_KWH = 0.75

# 3. Processamento dos dados (Cálculos de consumo e custo)
consumo_mensal = (potencia * horas_dia * 30) / 1000
custo_estimado = consumo_mensal * VALOR_KWH

# 4. Exibição dos resultados formatados
print("\n" + "="*30)
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo mensal estimado: R$ {custo_estimado:.2f}")
print("="*30)
