'''
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
'''

### Primeira solução
numeros = [1, 2, 3]

def duplica(x):
    duplicado = f'{x} * 2 = {x*2}'
    return duplicado

def triplica(x):
    triplicado = f'{x} * 3 = {x*3}'
    return triplicado

def quadruplica(x):
    quadruplicado = f'{x} * 4 = {x*4}'
    return quadruplicado


for numero in numeros:
    print(duplica(numero))
    print(triplica(numero))
    print(quadruplica(numero))

### Segunda solução
def operacoes(x):
    duplo = f'{x} * 2 = {x*2}'
    triplo = f'{x} * 3 = {x*3}'
    quadruplo = f'{x} * 4 = {x*4}'
    resultados = [duplo, triplo, quadruplo]
    return resultados

print(operacoes(5))

###Solução do otávio

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(2))
print(triplicar(3))
print(triplicar(4))


    


    




            

