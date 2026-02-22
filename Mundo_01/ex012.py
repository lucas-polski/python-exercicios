p = float(input('Digite o preço do produto: R$'))
d = p - (p * 5 / 100)
print(f'R${p:.2f} com 5% de desconto vai custar R${d:.2f}')