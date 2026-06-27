''' 
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar.
Caso o usuário não digite um número inteiro, informe que não é um número inteiro.
'''
# MINHA SOLUÇÃO

numero = (input("Digite um número inteiro:\t"))

if not numero.isdigit():
    print("Você não digitou um número inteiro")
else:
    numero_int = int(numero)
    numero_par = numero_int % 2 == 0
    if numero_par:
        print("Você digitou um número par")
    else:
        print("Você digitou um número ímpar")

# SOLUÇÃO COM TRY

numero = input("Digite um número inteiro ")

try:
    numero_int = int(numero)
    numero_par = numero_int % 2 == 0

    if numero_par:
        print('Você digitou um número par')
    else:
        print('Você digitou um número ímpar')
except:
    print("Você não digitou um número inteiro")



'''
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito,
exiba a saudação apropriada:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
'''

# MINHA SOLUÇÃO

hora = int(input("Que horas são? "))

if hora >= 0 and hora <= 11:
    print("Bom dia!")
elif hora >= 12 and hora <= 17:
    print("Boa tarde!")
elif hora >= 18 and hora <= 23:
    print("Boa noite!") 

# SOLUÇÃO DO OTÁVIO

entrada = input("Digite a hora em números inteiros: ")
try: # O try serve e except servem para tratar erros, pois o usuário pode digitar algo quenão pode virar inteiro
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print("Bom dia!")
    elif hora >= 12 and hora <= 17:
        print("Boa tarde!")
    elif hora >= 18 and hora <= 23:
        print("Boa noite!")
    else: 
        print("Não conheço essa hora!")
except:
    print("Por favor, digite um número inteiro")

'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos,
escreva "Seu nome é curto"; se tiver entre 5 e 6 letrar, escreva "Seu nome é normal;
maior que 6 escreva "Seu nome é muito grande
'''

# MINHA SOLUÇÃO

nome = input("Digite seu primeiro nome ")
contagem = len(nome)

if contagem <= 4:
    print("Seu nome é pequeno")
elif contagem >= 5 and contagem <= 6:
    print("Seu nome é normal")
elif contagem > 6:
    print("Seu nome é grande")

# Solução do Otávio

nome = input("Digite seu primeiro nome ")
contagem = len(nome)

if contagem > 1:
    if contagem <= 4:
        print("Seu nome é curto")
    elif contagem >= 5 and contagem <=6:
        print("Seu nome é normal")
    else:
        print("Seu nome é grande")
else: 
    print("Digite mais de uma letra.")


