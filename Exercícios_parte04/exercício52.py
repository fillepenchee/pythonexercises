
amigo1 = float(input(f'Valor da aposta do Amigo 1:'))
amigo2 = float(input(f'Valor da aposta do Amigo 2:'))
amigo3 = float(input(f'Valor da aposta do Amigo 3:'))
valorpremio = float(input(f'Digite o valor do prêmio:'))

totalaposta = (amigo1 + amigo2 + amigo3)

porcentamigo1 = (amigo1 / totalaposta)
porcentamigo2 = (amigo2 / totalaposta)
porcentamigo3 = (amigo3 / totalaposta)

retorno1 = (valorpremio * porcentamigo1)
retorno2 = (valorpremio * porcentamigo2)
retorno3 = (valorpremio * porcentamigo3)

print(f'O Amigo 1 ganhará {retorno1} reais, o Amigo 2 ganhará {retorno2} reais e o Amigo 3 ganhará'
      f' {retorno3} reais.')