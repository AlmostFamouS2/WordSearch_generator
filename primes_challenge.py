#!/usr/bin/env python3

# https://www.wechall.net/challenge/training/prime_factory/index.php

'''
Your task is simple:
Find the first two primes above 1 million, whose separate digit sums are also prime.
As example take 23, which is a prime whose digit sum, 5, is also prime.
The solution is the concatination of the two numbers,
Example: If the first number is 1,234,567
and the second is 8,765,432,
your solution is 12345678765432
'''

def isPrime(num):
    if num % 2 == 0:
        return False

    for n in range(3, int(num ** 0.5) + 1, 2):
        if num % n == 0:
            return False
    return True

def resolve(num):
    while True:
        # s = sum(list(map(lambda x: int(x), (list(num)))))
        s = sum(map(int, str(num)))
        print(s) #   Only if you want to VERBOSE MODE

        if isPrime(num) and isPrime(s):
            return num

        num += 2  # ELSE


def start():
    number = 1000001  # 1 milion

    n1 = resolve(number)
    n2 = resolve(n1+2)

    print(str(n1) + '   ' + str(n2))
    print(str(n1)+str(n2))

start()
