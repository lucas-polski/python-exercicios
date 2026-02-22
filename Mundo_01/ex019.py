import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))
lista_alunos = [n1 , n2 , n3 , n4]
aluno_sorteado = random.choice(lista_alunos)
print(f'O aluno sorteado foi {aluno_sorteado}')