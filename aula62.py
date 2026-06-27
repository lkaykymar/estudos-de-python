'''
Escopo de funções em python
escopo significa o local onde aquele código pode atingir
existe o escopo global e local
o escopo global é o escopo onde todo o código é alcançável
o escopolocal é o escopo onde apenas nomes do mesmo local
podem ser alcançados

não temos acesso a nomes de escopos internos nos escopos externos
a palavra global faz uma variável do escopo externo
ser a mesma no escopo interno

O valor global que vai valer é o valor de x mais próximo
parâmetros também faz parte do escopo da função

global é uma má prática

Uma call stack é uma pilha de mundos criados para cada escopo, por isso mesmo nome numa variável não 
da ruim
'''

x = 1

def escopo():
    #global x 
    x = 10 
    def outra_funcao():
        #global x 
        x = 11
        y = 2 
        print(x, y) 

    outra_funcao() 
    print(x)

print(x)
escopo()
print(x) 
