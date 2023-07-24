
idade = int(input('Qual a idade do trabalhador? \n'))
tempserv = int(input('Qual o tempo de serviço do trabalhador? \n'))

if idade >= 65 or tempserv >= 30:
    print('O trabalhador pode se aposentar.')

if idade < 60 or tempserv < 25:
    print('O trabalhador ainda não pode se aposentar.')

if idade >= 60 and tempserv >= 25:
    print('O trabalhador pode se aposentar.')
