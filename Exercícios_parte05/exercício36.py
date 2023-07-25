
venda = float(input('Digite o valor da venda mensal do vendedor (R$): \n'))

if venda >= 100000.00:
    comissao = 700 + (venda * 0.16)
elif 80000.00 <= venda <= 100000.00:
    comissao = 650 + (venda * 0.14)
elif 60000.00 <= venda <= 80000.00:
    comissao = 600 + (venda * 0.14)
elif 40000.00 <= venda <= 60000.00:
    comissao = 550 + (venda * 0.14)
elif 20000.00 <= venda <= 40000.00:
    comissao = 500 + (venda * 0.14)
elif venda <= 20000.00:
    comissao = 400 + (venda * 0.14)

print(f'A comissão do vendedor será de R$ {comissao}.')
