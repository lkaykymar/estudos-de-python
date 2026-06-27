# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
# Se você fizer ifs com esses valores, eles serão considerados falsos

# Tudo abaixo é falso, qualquer coisa diferente, é verdadeira
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

# Tudo abaixo é verdadeiro
lista2 = [1]
dicionario2 = {1}
conjunto2 = set((3, 4))
tupla2 = (1)
string2 = 'k'
inteito2 = 1
flutuante2 = 0.1
nada2 = 4
falso2 = True
intervalo2 = range(1)


def falsy(valor):
    return 'falsy'if not valor else 'truthy'


print(f'TESTE DOS FALSOS', falsy('TESTES FALSOS'))
print(f'{lista=}', falsy(lista))
print(f'{dicionario=}', falsy(dicionario))
print(f'{conjunto=}', falsy(conjunto))
print(f'{tupla=}', falsy(tupla))
print(f'{string=}', falsy(string))
print(f'{inteito=}', falsy(inteito))
print(f'{flutuante=}', falsy(flutuante))
print(f'{nada=}', falsy(nada))
print(f'{falso=}', falsy(falso))
print(f'{intervalo=}', falsy(intervalo),'\n')

print(f'TESTE DOS VERDADEIROS', falsy('TESTE VERDADEIROS'))
print(f'{lista2=}', falsy(lista2))
print(f'{dicionario2=}', falsy(dicionario2))
print(f'{conjunto2=}', falsy(conjunto2))
print(f'{tupla2=}', falsy(tupla2))
print(f'{string2=}', falsy(string2))
print(f'{inteito2=}', falsy(inteito2))
print(f'{flutuante2=}', falsy(flutuante2))
print(f'{nada2=}', falsy(nada2))
print(f'{falso2=}', falsy(falso2))
print(f'{intervalo2=}', falsy(intervalo2))