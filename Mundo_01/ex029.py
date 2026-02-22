vel = float(input('Qual a velocidade do carro: '))
if vel >= 79:
    print(f'Sua velocidade foi {vel:.1f} Então você foi multado!!')
    print(f'Sua multa será de 7,00 a cada km ultrapassado e Custará:')
    print(f'Um total de: {7 * (vel - 79):.2f}R$')
else:
    print('Sua velocidade não ultrapassou o limite de velocidade!')