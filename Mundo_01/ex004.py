#Dessecando uma variável
algo = input('Digite algo: ')
print(f'Seu tipo primitivo é {type(algo)}')
print('É numérico:', algo.isnumeric())
print('É um espaço:', algo.isspace())
print('É alfabeto:', algo.isalpha())
print('É alfanumérico:', algo.isalnum())