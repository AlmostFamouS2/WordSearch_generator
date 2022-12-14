#!/usr/bin/env python3
from random import randint
import numpy as np

def print_arr(array_grid):

    print('\n        ', end='')
    for n1 in array_grid:
        for n2 in n1:
           print(n2, end=' ')
        print('\n        ', end='')

def V_or_H(array_grid, words):

    for n in range(len(words)):
        decision = randint(0,1)
        if decision == 0:  # Horizontal
            X = randint(0,50-len(words[n]))  # X
            Y = randint(0,20-len(words[n]))   # Y
            array_grid[Y , X:X+len(words[n])] = [x for x in words[n]]    # (Coluna , linha)

        else:
            X = randint(0,50-len(words[n]))  # X
            Y = randint(0,20-len(words[n]))   # Y
            array_grid[Y:Y+len(words[n]), X ] = [x for x in words[n]]    # (Coluna , linha)
    print_arr(array_grid)

def generate(file):
    try:
        with open(file, 'r') as f:
            words = f.readlines()
            if len(words) > 5:
                print('Melhor fazer com menos que 5 palavras')
                exit(0)
            for n in range(len(words)):
                words[n] = words[n][:-1]
            print(words)
    except:
        print('NAO FOI POSSIVEL ABRIR O ARQUIVO')
        exit(0)

    letters = [x for x in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
    array_grid = np.random.choice(letters, (20,50))

    V_or_H(array_grid, words) 
            
if __name__ == '__main__':
    generate('palavras.txt')
