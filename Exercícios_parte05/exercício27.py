
idade = int(input('Digite a idade do nadador: \n'))

if 5 <= idade <= 7:
    print('O nadador está na categoria Infantil A.')

if 8 <= idade <= 10:
    print('O nadador está na categoria Infantil B.')

if 11 <= idade <= 13:
    print('O nadador está na categoria Juvenil A.')

if 14 <= idade <= 17:
    print('O nadador está na categoria Juvenil B.')

if idade >= 18:
    print('O nadador está na categoria Sênior.')

if idade < 5:
    print('O nadador não chegou à idade mínima.')
    