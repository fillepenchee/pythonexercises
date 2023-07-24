
comprimento = int(input(f'Digite o comprimento do terreno:'))
largura = int(input(f'Digite a largura do terreno:'))
precotela = int(input(f'Digite o preço do metro quadrado de tela em reais:'))

print(f'O valor da tela para cercar o terreno será de {((comprimento * 2) + (largura * 2)) * precotela}')
