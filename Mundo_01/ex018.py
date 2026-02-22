from math import radians, sin, cos, tan
ang = float(input('digite o angulo em graus: '))
seno = sin(radians(ang))
coseno = cos(radians(ang))
tan = tan(radians(ang))
print(f'para angulo de {ang}:')
print(f'Seno: {seno:.2f}\nCoseno: {coseno:.2f}\nTangente: {tan:.2f}')
