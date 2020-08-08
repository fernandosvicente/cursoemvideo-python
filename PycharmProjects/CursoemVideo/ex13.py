#cont = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
#        'seis', 'sete', 'oito', 'nove', 'dez',
#        'onze', 'doze', 'treze', 'quartoze', 'quinze',
#        'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
#while True:
#    num = int(input('digite um numero entre 0 e 20: '))
#    if 0 <= num <= 20:
#        break
#print(f'voce digitou o numero {cont[num]}')



#times = ('brasil', 'alemanha', 'frança', 'holanda', 'argentina', 'paraguai',
#         'japao','espanha', 'mexico', 'uruguai', 'chile' )
#print('=-=' * 45)
#print(f'lista de times {times}')
#print('=-=' * 45)
#print(f'os 5 primeiros times sao: {times[0:5]}')
#print('=-=' * 45)
#print(f'os quatro ultimos colocados sao: {times[-4:]}')
#print('=-=' * 45)
#print(f'time em ordem alfabetica: {sorted(times)}')
#print('=-=' * 45)
#print(f'a localização do japao e : {times.index("japao")+1}')



#from random import randint
#n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
#print(f'os numeros escolhidos sao : {n}')
#print(f'o maior valor e: {max(n)}')
#print(f'o menor valor e: {min(n)}')



#num = (int(input('digite o numero')),
#       int(input('digite o numero')),
#       int(input('digite o numero')),
#       int(input('digite o numero')))
#print(f' os numeros digitados sao:{num}')
#print(f' o numero 9 apareceu {num.count(9)} vezes')
#if 3 in num:
#    print(f' o numero 3 apareceu na posicao {num.index(3)}')
#else:
#    print(' o valor 3 nao foi digitado')
#print('os valores pares digitados foram', end=' ')
#for n in num:
#    if n % 2 == 0:
#        print(n, end=' ')



#listagem = ('lapis', 1.75,
#            'caderno', 2,
#            'macarrrao', 2.5,
#            'papel', 3.9)
#print('-'*30)
#print(f'{"listagem preco":^30}'.upper())
#print('-'*30)
#for pos in range(0, len(listagem)):
#    if pos % 2 == 0:
#        print(f'{listagem[pos]:.<24}',end='')
#    else:
#        print(f'R${listagem[pos]:>5.2f}')



palavras = ('python', 'curso', 'programacao', 'java', 'lingc', 'algoritmo')
for n in palavras:
    print(f'\nna palavra {n.upper()} temos:', end=' ')
    for letra in n:
        if letra.lower() in 'aeiouAEIOU':
            print(letra, end=' ')
