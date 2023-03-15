#!/usr/bin/env python3
from time import sleep
from sys import argv

if len(argv) == 1:
    print(f'\033[31mDigite um valor de andares do predio! \n  Exemplo: {argv[0]} 7  # Caso seja 7 andares\033[0m')
    exit(1)

def square( n = 1):
    print((' '*20 + '_'*25)*n)
    for x in range(0,10):
        print((' '*20 + '|' + ' '*23 + '|')*n)
        sleep(.1)
    print((' '*20 + '-'*25)*n)

for x in range(1, int(argv[1]) + 1):
    print(f'QUADRADO NUMERO: {x}')
    square(3)

#  ESTILO DOS DO WINDOWS :P

mensagem = input('DIGITE UMA MENSAGEM: ')

def IMPRIME(word):
    tam = len(word)
    print('='* (tam+9))
    print('   ' + word)
    print('='* (tam+9))

# IMPRIME('NARUTO GOSTA DE DETONAR')
IMPRIME(mensagem)
