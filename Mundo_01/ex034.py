sal = int(input('Qual o seu salario?'))
if sal > 1250:
    sal1 = sal + (sal * 10 / 100)
if sal <= 1250:
    sal1 = sal + (sal * 15 / 100)
print(f'seu salário de {sal} passa a ser de R$ {sal1:.2f}')
