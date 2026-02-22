from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista_alunos = [n1 , n2 , n3 , n4]
print(f'Ordem atual {lista_alunos}')
shuffle(lista_alunos)
print(f'Nova ordem ficou {lista_alunos}')