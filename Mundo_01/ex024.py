nome = str(input("Digite o nome de sua cidade: ")).strip()
#nome = nome.split()
nome11 = "santo"
nome1 = (nome[0])
if nome11 in nome1:
    print(f"Sua cidade começa com {nome11}")
else:
    print(f"Sua cidade não começa com {nome11}")
print(nome[:5].upper() == 'SANTO')