

### Parando o laço com break

contador = 0

while contador <= 10:
    contador += 1
    print(contador)

    if contador == 4:
        break

print('Acabou')
print('                         ')
print('-------------------------')
print('                         ')

### Escolhendo partes para pular usando continue

contador = 0

while contador <= 100: 
    contador += 1 # Vai contar até 100

    if contador == 6:
        continue # vai  pular o 6
    
    if contador >= 10 and contador <= 27:
        print("Pulado") # só pra visualizar melhor
        continue # vai pular os números nesse intervalo

    print(contador)

    if contador == 40:
        break # quandochegar no 40 o laço acaba

print('Acabou')


