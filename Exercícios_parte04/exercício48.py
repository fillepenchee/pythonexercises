
seg = int(input(f'Digite um número inteiro de segundos:'))

minu = (seg / 60)

hora = (minu / 60)

dia = (hora / 24)

print(f'{seg} segundo(s) equivale a {minu} minuto(s), {hora} hora(s) ou {dia} dia(s).')
