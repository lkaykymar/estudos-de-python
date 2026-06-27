"""
Interpolação básica de strings ( Mesma utilidade do format, mas diferente)

s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456789)

"""

nome = "Kayky"
preco = 1000.95897643
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)  #use o % e a letra do tipo
print(variavel)

# Converte pra hexadecimal minúsculo usando d
print("O hexadecimal de %d é %x" % (15, 15))

# Converte pra hexadecimal minúsculo usando i
print("O hexadecimal de %i é %x" % (15, 15))

# Converte pra hexadecimal maiúsculo
print("O hexadecimal de %d é %X" % (15, 15))

# Coloca 4 casas decimais no hexadecimal
print("O hexadecimal de %d é %04x" % (15, 15))

# Coloca 8 casas decimais no hexadecimal
print("O hexadecimal de %d é %08x" % (15, 15))

