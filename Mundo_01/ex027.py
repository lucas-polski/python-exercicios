n = str(input('Digite seu nome completo: ')).strip()#Lê o nome completo e remove espaços(.strip)
nome = n.split()#Divide a string em uma lista de palavras
print(f'Prazer em te conhecer {nome[0]}')
print(f'Seu ultimo nome é {nome[len(nome) -1]}')#mostra o último item, usando a função len() para contar e subtrair 1

