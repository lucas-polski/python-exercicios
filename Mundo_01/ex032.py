from datetime import date
ano = int(input('Digite o ano para analisar ou digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year#Pega o ano atual configurado na maquina
if ano % 4 == 0 and ano % 100 > 0 or ano % 400 == 0:
    print(f'o ano {ano} é bissexto!')
else:
    print(f'o ano {ano} não é bissexto')