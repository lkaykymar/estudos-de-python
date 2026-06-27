"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

##### MINHA RESOLUÇÃO
print('KAYKY')
cpf_1 = input('Digite seu CPF: ')
cpf_formatado_1 = ''
soma_cpf_1 = 0
contador_1 = 10
k_1 = 0

for i in cpf_1:
    if i.isdigit():
        cpf_formatado_1 += i

while contador_1 > 2:
    valor_1 = int(cpf_formatado_1[k_1])
    multiplicacao_1 = valor_1 * contador_1
    soma_cpf_1 += multiplicacao_1
    contador_1 -= 1
    k_1 += 1

multiplicacao_cpf_1 = soma_cpf_1 * 10
resto_divisao_1 = multiplicacao_cpf_1 % 11

if resto_divisao_1 > 9:
    print(f'O primiro dígito do cpf é: 0')
else:
    print(f'O primiro dígito do cpf é: {resto_divisao_1}')

resto_divisao_str = str(resto_divisao_1)
cpf_2 = cpf_formatado_1[:9]
cpf_2 = cpf_2 + resto_divisao_str
contador_2 = 11
k_2 = 0
soma_cpf_2 = 0

while contador_2 > 1:
    valor_2 = int(cpf_2[k_2])
    multiplicacao_2 = valor_2 * contador_2
    soma_cpf_2 += multiplicacao_2
    contador_2 -= 1
    k_2 += 1

multiplicacao_cpf_2 = soma_cpf_2 * 10
resto_divisao_2 = multiplicacao_cpf_2 % 11

digito_2 = resto_divisao_2 if resto_divisao_2 <= 9 else 0
print('O segundo digito do cpf é:', digito_2)

digito_2_str = str(digito_2)
cpf_2 = cpf_2 + digito_2_str
print(cpf_2)

if cpf_2 == cpf_formatado_1:
    print('CPF VÁLIDO')
else:
    print('CPF INVÁLIDO')









