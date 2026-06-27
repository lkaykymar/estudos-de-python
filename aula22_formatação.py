"""
Formatação básica de strings

s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(Quantidade)
> - Esquerda
< - Direita
^ - Centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a

"""

variavel = "ABC"

# Podemos preencher espaços
print(f"{variavel:x<10}")
print(f"{variavel:v>10}") #10 contando com as letras da variável
print(f"{variavel:v^10}") 
print(f"{variavel: ^10}") 
print(f"{1000.054544578568974455:,.2f}") 
print(f"{-1000.054544578568974455:,.2f}") 
print(f"{1000.054544578568974455:+,.2f}") # Faz com que só mostre o sinal se for positivo
print(f"{1000.054544578568974455:-,.2f}") # Faz com que só mostre o sinal se for negativo
print(f"{1000.054544578568974455:0>+100,.2f}") # 
print(f"{1000.054544578568974455:0=+100,.2f}") # Força o número a aparecer depois dos zeros