#Operador in e not in (esta entre e não esta entre)
# Strings são iteráveis (Voce pode no python, navegar intem por intem)
# 0 1 2 3 4 
# K a y k y
#-5-4-3-2-1

nome = "Kayky"
print(nome[0])
print(nome[1])
print(nome[2])
print(nome[-2])
print(nome[-3])

# Voce pode checar se uma letra qualquer está entre as letras da string
print("k" in nome)
print("o" in nome)
print("ka" in nome)
print("yky" in nome)
print("zero" in nome)
print("k" not in nome)

#brincadeira:

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else: 
    print(f"{encontrar} não está em {nome}")