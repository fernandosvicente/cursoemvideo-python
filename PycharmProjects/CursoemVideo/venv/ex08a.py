import math
from symbol import import_as_name

num = int(input('digite um numero: '))
raiz = math.sqrt(num)
print('a raiz de {} é igual a {}'. format(num, math.ceil(raiz)))
print('a raiz de {} é igual a {}'. format(num, math.floor(raiz)))
print('a raiz de {} é igual a {:.2f}'. format(num, raiz))

import math
tot = float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(tot, math.trunc(tot)))

from math import trunc
tot = float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(tot, trunc(tot)))

tot = float(input('digite um valor: '))
print('o valor digitado foi {} e a sua porção inteira é {}'. format(tot, int(tot)))

co = float(input('comprimento do cateto oposto: '))
ca = float(input('comprimento do cateto adjacente: '))
hi = (co**2 + ca**2)**(1/2)
print('a hipotenusa vai medir {:.2f}'.format(hi))

import math
co = float(input('o comprimento do cateto oposto: '))
ca = float(input('o comprimento do cateto adjavente: '))
hi = math.hypot(co, ca)
print('a hipotenusa vai medir {:.2f}'.format(hi))

import math
angulo = float(input('digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem o sen de {:.2f}, cos de {:.2f}, tan de {:.2f}'.format(angulo, seno, cosseno, tangente))

import random
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceitro aluno: '))
n4 = str(input('quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('o aluno escolhido foi {}'.format(escolhido))
random.shuffle(lista)
print('a ordem de apresentação será ')
print(lista)

'''tocar mp3 musica primeiro salva o nome da musica como ex021 e copiar e colar no programa python depois escrever
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

