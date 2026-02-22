dis = int(input('Digite a distância em km: '))
if dis <= 200:
    preço = dis * 0.50
else:
    preço = dis * 0.45
print(f'Sua viagem custará {preço}')
