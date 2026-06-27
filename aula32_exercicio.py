# MINHA RESOLUÇÃO

nome = 'Kayky Lourenço Martins'
tamanho_final = (len(nome)*2) + 1
position2 = 0

while position2 < tamanho_final:
    nome = f'{nome[ :position2]}*{nome[position2: ]}'
    print(nome)
    position2 += 2

print("Acabou")

# RESOLUÇÃO DO OTÁVIO (usando conceito de acumulação)

nome = 'Cicero Lourenço'

indice = 0
novo_nome = '' #acumulador
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

print(novo_nome)


    
        
 


