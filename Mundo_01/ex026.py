frase = str(input("Digite uma frase ").strip().lower())
a = frase.count("a")
primeira = frase.find("a")+1
ultima = frase.rfind("a")+1
print(f"Apareceram {a} A, primeiro indice foi em {primeira} e a ultima vez foi em {ultima}")