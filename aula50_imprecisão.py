'''
Imprecisão de ponto flutuante
double precision floating-point format IEEE 754

'''
numero_1 = 0.1
numero_2 = 0.7
numero_3 = numero_1 + numero_2
print(numero_3)

# Na maioria das vezes não da problema, ja que quase emore a gente formata 
print(f'{numero_3:.2f}')

# round formata também
print(round(numero_3, 2))
print(round(numero_3, 3))
print(round(numero_3, 4)) # 4 casas decimais mas todas zero, por isso não aparece

import decimal

numero_4 = decimal.Decimal(0.1)
numero_5 = decimal.Decimal(0.7)
numero_6 = numero_4 + numero_5
print(numero_6)