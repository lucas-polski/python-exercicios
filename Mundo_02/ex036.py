valor_casa = float(input('Qual o valor da casa: '))
salario = float(input('Qual seu salário: '))
anos = int(input('Em quantos anos deseja pagar: '))
#prestacao = valor_casa / (anos * 12)
#salario30 = salario * 30 / 100
print(f'O valor da parcela não pode ser maior do que {salario * 30 / 100:.2f}')
print(f'Certo! sua prestação será de R$ {valor_casa / (anos * 12):.2f}')
if valor_casa / (anos * 12) > salario * 30 / 100:
    print('Infelizmente não podemos aprovar o empréstimo ;(')
else:
    print('Parabéns, seu empréstimo foi aprovado!')
print('Fim da avaliação!')