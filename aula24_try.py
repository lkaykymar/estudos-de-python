'''
Introdução ao try/except: 
try -> tentar executar o código
except -> ocoreu algum erro ao tentar executar

'''

numero = input('Vou dobrar o numero que voce digitar: ')
numero_float = float(numero)
print(numero.isdigit()) # Esse isdigit confere se o usuário digitou apenas números 

if numero.isdigit():
    print(f'O dobro do numero {numero} é {numero_float * 2}')
else: 
    print('Isso não é um numero')



try:
    numero_float = float(numero)
    print(f'Float: {numero_float}')
    print(f'O dobro de {numero_float} é {numero_float*2}')
except:
    print('Isso não é um numero')

print(123)
print(456)
int('a') # aqui ocorreu um except



