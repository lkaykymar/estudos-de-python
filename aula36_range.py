'''
for + range (Não dependem um do outro)
range -> range(start, stop, step)

'''
'''Quando voce passa um valor, esse valor é onde ele vai terminar,
 começando do zero e pulando de um em um'''
numeros_1 = range(10)
print(numeros_1)

'''Quando você passa dois valores, o primeiro é o inicio e o segundo é o fim (que não é incluído)
e pulando de um em um'''
numeros_2 = range(5, 10)
print(numeros_2)

'''Quando voce passa 3 numeros, voce determina o ínicio, fim e de quanto em quanto ele vai pular'''
numeros_3 = range(5, 10, 2)
print(numeros_3)

# o for não vai no íncide como no while, vai direto no valor
numeros_3 = range(2, 10, 3)
print(numeros_3)

for numero in numeros_3:
    print(numero)


