
chegada = input('Digite o horário de chegada (hh:mm): \n')
saida = input('Digite o horário de saída (hh:mm): \n')

horacheg, mincheg = chegada.split(':')
horacheg = int(horacheg)
mincheg = int(mincheg)

horasai, minsai = saida.split(':')
horasai = int(horasai)
minsai = int(minsai)

if (minsai - mincheg) > 0 and (horasai - horacheg) > 0:
    tempo = (horasai - horacheg) + 1
elif (minsai - mincheg) <= 0 and (horasai - horacheg) > 0:
    tempo = (horasai - horacheg) - 1
elif (minsai - mincheg) > 0 and (horasai - horacheg) < 0:
    tempo = (horasai - horacheg) - 1
elif (minsai - mincheg) <= 0 and (horasai - horacheg) < 0:
    tempo = (horasai - horacheg) + 1
else:
    tempo = (horasai - horacheg)

if tempo < 0:
    tempo = -tempo
if tempo == 0:
    tempo = tempo + 1

if tempo <= 2:
    preco = 1.00 * tempo
elif 2 < tempo < 4:
    preco = 2.00 + (1.40 * (tempo - 2))
else:
    preco = 4.80 + (2.00 * (tempo - 4))

print(f'Você ficou {tempo} hora(s) no estacionamento. O preço a pagar é de R$ {preco}.')

