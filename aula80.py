# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

# Você pode operar esses sets pelos nomes ou símbolos
# Unindo os dois
s3 = s1.union(s2)
print(s3)

# Intersectando os dois
s4 = s1.intersection(s2)
print(s4)

# Pegando itens presentes apenas na esquerda e direita
s5 = s1.difference(s2) # Esquerda
print(s5)

s6 = s2.difference(s1) # Direita
print(s6)

# Diferença simétrica
s7 = s1.symmetric_difference(s2)
print(s7)

# Usando os símbolos agora
# Unindo
s10 = s1 | s2
print(s10)

# Intersectando
s11 = s1 & s2
print(s11)

# Diferença
s12 = s1 - s2
print(s12)

s13 = s2 - s1
print(s13)

#Diferença simétrica
s14 = s1 ^ s2
print(s14)
