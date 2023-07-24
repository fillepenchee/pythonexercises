
hora = int(input(f'Digite a hora em que começou o experimento:'))

minuto = int(input(f'Digite o minuto em que começou o experimento:'))

segundo = int(input(f'Digite o segundo em que começou o experimento:'))

duracao = int(input(f'Digite quantos segundos durou o experimento:'))

hora2 = int((duracao / 3600))

minuto2 = int((duracao / 60) - (hora2 * 60))

segundo2 = duracao - (minuto2 * 60)

tempoemsegundos = duracao + hora2 + minuto2 + segundo2

hora3 = int(tempoemsegundos / 3600)

minuto3 = int((tempoemsegundos / 60) - (hora3 * 60))

segundo3 = tempoemsegundos - (hora3 * 3600)

print(f'O experimento terminou às {hora3} hora(s), {minuto3} minuto(s) e {segundo3} segundo(s).')
