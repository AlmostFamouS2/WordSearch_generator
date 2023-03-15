#!/usr/bin/env python3
from datetime import datetime
def func():
    for n in range(50000000):
        if n % 7 == 0:
            pass
        elif n % 35:
            pass
        else:
            pass

from time import sleep
start = datetime.now()

#for n in range(50000000):
    #if n % 7 == 0:
        #pass
    #elif n % 35:
        #pass
    #else:
        #pass
#
#print(datetime.now() - start)

func()

#from dis import dis
#print('\x1b[31m')
#print(dis(func))
#print('\x1b[32m' + '-'*70 + '\n\n')
#print(dis('''for n in range(50000000):
    #if n % 7 == 0:
        #pass
    #elif n % 35:
        #pass
    #else:
        #pass'''))
print(f"Took: {str(datetime.now() - start)[5:-3].replace('.', 's ')}ms")
