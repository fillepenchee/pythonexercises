
peso = float(input('Digite o seu peso em kg: \n'))
altura = float(input('Digite a sua altura em m: \n'))
imc = (peso // (altura ** 2))

if imc < 18.5:
    categ = 'Abaixo do peso'
elif 18.6 < imc < 24.9:
    categ = 'Saudável'
elif 25.0 < imc < 29.9:
    categ = 'Peso em excesso'
elif 30.0 < imc < 34.9:
    categ = 'Obesidade grau I'
elif 35.0 < imc < 39.9:
    categ = 'Obesidade Grau II (Severa)'
else:
    categ = 'Obesidade Grau III (Mórbida)'

print(f'O seu IMC é {imc}, considerado "{categ}".')
