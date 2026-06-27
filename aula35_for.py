# Não é muito comum usar o while quando agente sabe quantas execuções, nesse caso 6

# texto = 'python'

# i = 0
# tamanho_texto = len(texto)

# while i < tamanho_texto:
#     print(texto[i], i)
#     i += 1

# O laço abaixo pode conter infinitas repetições
# Quando não sabemos quantas repetições vão ocorrer, usamoso while

senha_salva = '123456'
senha_digitada = '' 
repeticoes = 0

while senha_salva != senha_digitada:
    senha_digitada = input(f'Sua senha ({repeticoes}x): ')

    repeticoes += 1

print(repeticoes)
print('Aquele laço acima pode  ter repetições infinitas')

# O for é para quando sabemos a quantidade de repetições
# É iterável, voce passa um por um
# Para cada letra no texto, escreva essa letra
# O for armazena cada elemento do texto na variável que voce criar, nesse caso, letra. 

# segundo_texto = "Kayky" 

# texto_novo = ''
# for letra in texto: 
#     texto_novo += f'*{letra}'
#     print(letra)

# print(texto_novo)


