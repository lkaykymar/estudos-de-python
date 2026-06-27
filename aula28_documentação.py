'''
imutáveis que vimos: str, int, float, bool todos são objetos e tem ações que voce pode executar nelas

'''

string = 'kayky Martins' # Kayky martins é imutável
#string[3] = 'ABC' # Não consigo trocar a letra K por ABC, pois é imutável
#print(string[3])

# Você teria que criar outra variável

outra_variavel = f'{string[:3]}ABC{string[3:]}'
print(outra_variavel)
print(outra_variavel.capitalize()) # Traz a letra maiúscula 
print(outra_variavel.zfill(100)) # Se a string não tiver caracterees, ele preenche com 0 do lado esquerdo

