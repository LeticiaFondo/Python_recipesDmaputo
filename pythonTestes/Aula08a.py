'''''

#importacao  de biblioteca
#aqui importa todas as funcionalidades
import math
num = int(input('Digite um numero'))
raiz = math.sqrt(num)
print('A raiz de {} e de {}.'.format(num, math.ceil(raiz)))
#ceil = arredonda os numero para cima
#floor arredonda para baixo

from math import sqrt

num = int(input('digite um numero: '))
raiz = sqrt(num)
print('a raiz de {} e igual a {}.'.format(num, raiz))


import random
num = random.randint(1, 10)
print(num)
'''

import emoji
print(emoji.emojize('Ola mundo : thumbs_up:'))

