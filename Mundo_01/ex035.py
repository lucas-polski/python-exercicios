a = float(input('Lado A: '))
b = float(input('Lado B: '))
c = float(input('Lado C: '))
if a + b > c and a + c > b and b + c > a:
    print('É um triangulo!')
else:
    print('Não é um triangulo!')