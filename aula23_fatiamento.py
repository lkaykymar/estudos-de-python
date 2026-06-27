'''
Fatiamento de strings
 012345678 - índice
 Olá mundo
-987654321 - índice negativo
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a quantidade de caracteres da string

'''

variavel = 'Olá mundo'

print(variavel[-1]) # Pega um elemento da str
print(variavel[4:]) # Pega uma fatia, início, e quando não tem nada depois ele pega até o fim
print(variavel[:5]) # Mesma coisa mas ao contrário
print(variavel[4:7]) # Ele não inclui o último
print(variavel[3]) # O espaço vazio também conta no índice
print(variavel[-8:-4]) 

# Função len conta caracteres
print(len(variavel))
print(len(variavel[0:len(variavel):1]))# inicio, fim e de quanto em quanto ele vai pegar
print((variavel[0:9:1]))
print((variavel[0:9:2])) # passo de 2 em 2
print((variavel[0:9:3])) # passo de 3 em 3
print((variavel[-1:-10:-3])) # passo de 3 em 3 negativo