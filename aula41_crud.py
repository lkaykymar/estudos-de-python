###################### CRUD ( create, read, update and delete)
lista_1 = [123, True, ['Kayky', 'Júlia', 18.1], 'lourenço', 45.5] # Create
lista_1[3] = 'Martins'                                            # Update
del lista_1[2]                                                    # Delete
lista_1.pop()                                                     # Remove o último
lista_1.append(555555555)                                         # Append
print(f'Create, update, delete and append: {lista_1}\n')

# É possível remover o elemento com pop e jogar ele em uma variável
lista_2 = [123, True, ['Kayky', 'Júlia', 18.1], 'lourenço', 45.5]
numero = lista_2.pop()
print(f'Elemento removido: {numero}\n')

# É possível limpar a lista com clear
lista_3 = [123, True, ['Kayky', 'Júlia', 18.1], 'lourenço', 45.5]
lista_3.clear()
print(f'Lista limpa: {lista_3}\n')

# Insert serve pra adicionar um elemento onde quiser
lista_4 = [123, True, ['Kayky', 'Júlia', 18.1], 'lourenço', 45.5]
lista_4.insert(0 , 'Margarida') # Onde vai entrar e oq vai entrar
print(f'Usando insert: {lista_4}')

