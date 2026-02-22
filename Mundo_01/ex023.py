NUMERO = int(input("Digite um numero: "))
#NUMEROESP = " ".join(NUMERO)
#NUMERODIV = NUMEROESP.split()
#print(f"MILHAR: {NUMERODIV[0]}")
#print(f"CENTENA: {NUMERODIV[1]}")
#print(f"DEZENA: {NUMERODIV[2]}")
#print(f"UNIDADE: {NUMERODIV[3]}")
#resolução guabanara abaixo:
#n = str(NUMERO)
u = NUMERO // 1 % 10
d = NUMERO // 10 % 10
c = NUMERO // 100 % 10
m = NUMERO // 1000 % 10
print(f'Analisando o numero {NUMERO} ...')
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

