'''
Closure e funções que retornam outras funções

Uma função interna que é definida dentro de outra função “lembra” das variáveis do escopo da função externa, 
mesmo depois que a função externa terminou de ser executada.
'''

'''S e precisassemos criar saudações pra cada pessoa, seria muitas,
podemos facilitar com closure'''

'''
Aqui entra o conceito de closure:

A função interna (saudar) “lembra” do valor da variável saudacao da função externa,
 mesmo depois que a função externa (criar_saudacao) terminou de ser executada.

Ou seja, saudar mantém acesso a saudacao — isso é o que chamamos de closure.
'''

nomes = ['Kayky', 'Lourenço', 'Martins']

def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in nomes:
    print(falar_bom_dia(nome))