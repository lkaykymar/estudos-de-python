'''
Escopo de funções em python
escopo significa o local onde aquele código pode atingir
existe o escopo global e local
o escopo global é o escopo onde todo o código é alcançável
o escopolocal é o escopo onde apenas nomes do mesmo local
podem ser alcançados
'''

# Se tenho um escopo fechado dentro de ma função, o código não vai afetar o que está fora da função
# Oq está dentro da função fica la, está protegido



# A variável x está dentro do escopo da função escopo
# Não da pra acessar o x fora do escopo
# Para isso você deve definir a variável no escopo externo

x = 1

def escopo():
    global x # agora o x seguinte é o mesmo do fora do escopo
    x = 10 # Esse x não é o x do inicio, apesar do mesmo nome, pq está protegido
    def outra_funcao():
        global x # Como esse é o último global, todos os x vão valer 11
        x = 11
        y = 2 # isso está preso no escopo outra função
        print(x, y) # Isso está preso no escopo outra função

    outra_funcao() # Só pode ser executado dentro do escopo de outra função
    print(x)

print(x)
escopo()
print(x) # Esse é o x inicial, pois está fora da função
