
count = 0
soma = 0

while True:
    i = int(input('Digite notas no intervalo de 10 a 20: \n'
                  'Digite qualquer outro número para saber a média e '
                  'encerrar o programa. \n'))
    if i in range(10, 21):
        soma = soma + i
        count = count + 1
    else:
        print("Este valor está fora do intervalo.")
        if count == 0:
            print('Como o valor da nota é inválido, sua média é 0.')
        else:
            media = (soma / count)
            print(f'A média aritmética é {media}.')
        break
