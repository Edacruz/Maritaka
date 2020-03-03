from random import choice

numero = [0,1,2,3,4,5,6,7,8,9]
sekai = choice(numero)

sua_escolha = int(input('Digite um número: '))

if sua_escolha == sekai:
    print('você ganhou! ')
else:
    print('você não é tão bom assim é um fracassado!')


