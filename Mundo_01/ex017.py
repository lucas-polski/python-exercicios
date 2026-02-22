from math import hypot
'''ca = float(input('informe o cateto adjacente: '))
co = float(input('informe o cateto oposto: '))
hip = ((ca**2) + (co**2))**(1/2)
print(f'o valor da hipotenusa é {hip:.2f}')'''
ca = float(input('informe o cateto adjacente: '))
co = float(input('informe o cateto oposto: '))
hip = hypot(ca, co)
print(f'a hipotenusa tem o valor {hip:.2f}')