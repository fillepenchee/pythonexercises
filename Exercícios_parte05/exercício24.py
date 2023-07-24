
valor = float(input('Digite o valor do produto: \n'))
estado = int(input('Digite o número do estado destino: \n 1-Minas Gerais \n 2-Rio de Janeiro \n'
               '3-São Paulo \n 4- Mato Grosso do Sul: \n'))

while 1 < estado > 4:
    print('O número de estado digitado é inválido.')
    estado = int(input('Digite um número de estado válido: \n'))

if estado == 1:
    print(f'O valor final do produto é {valor + (0.07 * valor)}.')

if estado == 2:
    print(f'O valor final do produto é {valor + (0.15 * valor)}.')

if estado == 3:
    print(f'O valor final do produto é {valor + (0.12 * valor)}.')

if estado == 4:
    print(f'O valor final do produto é {valor + (0.08 * valor)}.')
